from hamcrest import assert_that, has_properties
import json
from dm_api_account.models import ChangeEmail
from dm_api_account.models.user_envelope import UserRole, Rating


def test_put_v1_account_email(dm_api_facade, prepare_user, status_code=201):
    login = prepare_user.login
    email = prepare_user.email
    password = prepare_user.password

    dm_api_facade.account.register_new_user(
        login=login,
        email=email,
        password=password,
        status_code=status_code
    )

    dm_api_facade.account.activate_registered_user(login=login)

    data = ChangeEmail(
        login=login,
        email="User_Test6@mail.ru",
        password=password
    )

    response = dm_api_facade.account_api.put_v1_account_email(json=data)
    # print(json.loads(response.json(by_alias=True, exclude_none=True)))
    assert_that(response.resource, has_properties(
        {
            "login": login,
            "rating": Rating(
                enabled=True,
                quality=0,
                quantity=0
            ),
            "roles": [UserRole.GUEST, UserRole.PLAYER]
        }
    ))
