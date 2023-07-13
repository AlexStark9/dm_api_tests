from hamcrest import assert_that, has_properties
from dm_api_account.models.user_envelope import UserRole, Rating
from services.dm_api_account import Facade
import structlog
from dm_api_account.models.reset_password_model import ResetPassword

structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False)
    ]
)


def test_post_v1_account_password():
    api = Facade(host="http://localhost:5051")
    login = "Login_43"
    email = "Login_43@email.ru"
    password = "qwerty12345"

    api.account.register_new_user(
        login=login,
        email=email,
        password=password
    )

    api.account.activate_registered_user(login=login)

    json = ResetPassword(
        login=login,
        email=email
    )

    response = api.account_api.post_v1_account_password(json=json)

    # assert_that(response.resource, has_properties(
    #     {
    #         "login": login,
    #         "roles": [UserRole.GUEST, UserRole.PLAYER],
    #         "rating": [Rating.enabled, Rating.quality, Rating.quantity]
    #     }
    # ))
