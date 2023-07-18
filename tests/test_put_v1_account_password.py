import time

from hamcrest import assert_that, has_properties

from dm_api_account.models import ResetPassword
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
    login = "Login_6111126211"
    email = "Login_6111126211@email.ru"
    password = "qwerty12345"
    new_password = "12345qwerty11"

    api.account.register_new_user(
        login=login,
        email=email,
        password=password
    )

    api.account.activate_registered_user(login=login)

    token = api.login.get_auth_token(
        login=login,
        password=password
    )
    api.account.set_headers(headers=token)

    api.account.reset_password(
        login=login,
        email=email
    )
    time.sleep(3)

    api.account.change_password(
        login=login,
        password=password,
        new_password=new_password
    )

    # assert_that(response.resource, has_properties(
    #     {
    #         "login": login,
    #         "roles": [UserRole.GUEST, UserRole.PLAYER],
    #         "rating": [Rating.enabled, Rating.quality, Rating.quantity]
    #     }
    # ))
