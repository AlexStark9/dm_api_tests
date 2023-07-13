from services.dm_api_account import Facade
import structlog
from hamcrest import assert_that, has_properties
from dm_api_account.models.user_envelope import UserRole, Rating

structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False)
    ]
)


def test_put_v1_account_token():
    api = Facade(host="http://localhost:5051")
    login = "Login_19"
    email = "Login_19@email.ru"
    password = "qwerty12345"

    api.account.register_new_user(
        login=login,
        email=email,
        password=password
    )

    response = api.account.activate_registered_user(login=login)

    assert_that(response.resource, has_properties(
        {
            "login": login,
            "rating": [Rating.enabled, Rating.quality, Rating.quantity],
            "roles": [UserRole.GUEST, UserRole.PLAYER]
        }
    ))
