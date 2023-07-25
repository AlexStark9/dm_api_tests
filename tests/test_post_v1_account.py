import random
import time
from string import ascii_letters, digits
import pytest
from hamcrest import assert_that, has_entries


def random_string(begin, end):
    symbol = ascii_letters + digits
    string = ''
    for _ in range(random.randint(begin, end)):
        string += random.choice(symbol)
    return string


@pytest.mark.parametrize('login, email, password, status_code, check', [
    (random_string(5, 15),
     random_string(5, 15) + '@mail.com',
     random_string(6, 20), 201, 'Success'
     ),
    (random_string(5, 15),
     random_string(5, 15) + '@mail.com',
     random_string(1, 5), 400, {"Password": ["Short"]}
     ),
    (random_string(1, 1),
     random_string(5, 15) + '@mail.com',
     random_string(6, 20), 400, {"Login": ["Short"]}
     ),
    (random_string(5, 15),
     random_string(5, 15) + '@',
     random_string(5, 20), 400, {"Email": ['Invalid']}
     ),
    (random_string(5, 15),
     random_string(5, 15) + 'mail.com',
     random_string(6, 20), 400, {"Email": ['Invalid']}
     ),
])
def test_post_v1_account(dm_api_facade, dm_db, login, email, password, status_code, check):
    dm_db.delete_user_by_login(login=login)
    dataset = dm_db.get_users_by_login(login=login)
    assert len(dataset) == 0
    dm_api_facade.mailhog.delete_all_messages()
    response = dm_api_facade.account.register_new_user(
        login=login,
        email=email,
        password=password,
        status_code=status_code
    )
    if status_code == 201:
        dataset = dm_db.get_users_by_login(login=login)
        for row in dataset:
            assert_that(row, has_entries(
                {
                    'Login': login,
                    'Activated': False

                }
            ))

        # api.account.activate_registered_user(login=login)
        dm_db.activate_user_by_login(login=login)

        time.sleep(3)

        dataset = dm_db.get_users_by_login(login=login)
        for row in dataset:
            assert row['Activated'] is True, f'User {login} not activated'

        token = dm_api_facade.login.get_auth_token(login=login, password=password)
        dm_api_facade.account.set_headers(headers=token)
        dm_api_facade.account.get_current_user_info()
    else:
        if status_code != 201 and len(password) <= 5:
            response.json()['errors'], has_entries(
                {
                    'Password': check
                }
            )
        elif status_code != 201 and len(login) <= 1:
            response.json()['errors'], has_entries(
                {
                    'Login': check
                }
            )
        else:
            assert_that(response.json()['errors'], has_entries(
                {
                    'Email': check['Email']
                }
            ))
