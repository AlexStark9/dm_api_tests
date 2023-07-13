from hamcrest import assert_that, has_properties
from dm_api_account.models.user_envelope import UserRole, Rating
from services.dm_api_account import Facade
import structlog
from dm_api_account.models.change_email_model import ChangeEmail

structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False)
    ]
)


def test_put_v1_account_email():
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

    json = ChangeEmail(
        login=login,
        email="User_Test6@mail.ru",
        password=password
    )

    response = api.account_api.put_v1_account_email(json=json)

    assert_that(response.resource, has_properties(
        {
            "login": login,
            "roles": [UserRole.GUEST, UserRole.PLAYER],
            "rating": [Rating.enabled, Rating.quality, Rating.quantity]
        }
    ))
