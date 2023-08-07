import random
import time
from string import ascii_letters, digits
import allure
import pytest
from hamcrest import assert_that, has_entries
from generic.assertions.response_checker import check_status_code_http


def random_string(begin, end):
    symbol = ascii_letters + digits
    string = ''
    for _ in range(random.randint(begin, end)):
        string += random.choice(symbol)
    return string


@allure.suite("Тесты на проверку метода POST{host}/v1/account")
@allure.sub_suite("Позитивные проверки")
@allure.title("Проверка регистрации и активации пользователя на рандомных данных")
@allure.step("Подготовка тестового пользователя")
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
def test_post_v1_account(dm_api_facade, dm_db, login, email, password, status_code, check, assertion):
    dm_db.delete_user_by_login(login=login)
    dataset = dm_db.get_users_by_login(login=login)
    assert len(dataset) == 0
    dm_api_facade.mailhog.delete_all_messages()
    with check_status_code_http(expected_status_code=status_code, expected_result=check):
        dm_api_facade.account.register_new_user(
            login=login,
            email=email,
            password=password
        )

    if status_code == 201:
        assertion.check_user_was_created(login=login)
        # api.account.activate_registered_user(login=login)
        dm_db.activate_user_by_login(login=login)
        time.sleep(3)
        assertion.check_user_was_activated(login=login)
        token = dm_api_facade.login.get_auth_token(login=login, password=password)
        dm_api_facade.account.get_current_user_info(x_dm_auth_token=token)
