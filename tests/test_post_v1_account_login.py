from hamcrest import assert_that, has_properties
from dm_api_account.models.user_envelope import UserRole, Rating
from services.dm_api_account import Facade
import structlog


structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False)
    ]
)


def test_post_v1_account_login():
    """
    Authenticate via credentials
    :return:
    """
    api = Facade(host="http://localhost:5051")
    login = "Login_33"
    email = "Login_33@email.ru"
    password = "qwerty12345"

    api.account.register_new_user(
        login=login,
        email=email,
        password=password
    )

    api.account.activate_registered_user(login=login)

    response = api.login.login_user(
        login=login,
        password=password
    )

    assert_that(response.resource, has_properties(
        {
            "login": login,
            "roles": [UserRole.GUEST],
            "rating": [Rating.enabled, Rating.quality, Rating.quantity]
        }
    ))
