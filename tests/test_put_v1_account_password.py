from hamcrest import assert_that, has_properties
from dm_api_account.models.user_envelope import UserRole, Rating
from services.dm_api_account import Facade
import structlog
from dm_api_account.models.change_password_model import ChangePassword

structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False)
    ]
)


def test_put_v1_account_password():
    api = Facade(host="http://localhost:5051")
    login = "Login_44"
    email = "Login_44@email.ru"
    password = "qwerty12345"

    api.account.register_new_user(
        login=login,
        email=email,
        password=password
    )

    api.account.activate_registered_user(login=login)

    token = api.login.get_auth_token(login=login, password=password)

    json = ChangePassword(
        login=login,
        token=token,
        oldPassword=password,
        newPassword='12345qwerty11'
    )

    response = api.account_api.put_v1_account_password(json=json)

    # assert_that(response.resource, has_properties(
    #     {
    #         "login": login,
    #         "roles": [UserRole.GUEST, UserRole.PLAYER],
    #         "rating": [Rating.enabled, Rating.quality, Rating.quantity]
    #     }
    # ))
