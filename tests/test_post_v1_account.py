import time
from services.dm_api_account import DmApiAccount
from services.mailhog import MailhogApi
import structlog
from dm_api_account.models.registration_model import Registration
from hamcrest import assert_that, has_properties
from dm_api_account.models.user_envelope import UserRole, Rating

structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False)
    ]
)


def test_post_v1_account():
    mailhog = MailhogApi(host="http://localhost:5025")
    api = DmApiAccount(host="http://localhost:5051")
    json = Registration(
        login='Test_Testoviy',
        email="User_Test949@mail.ru",
        password="qwerty12345"
    )

    response = api.account.post_v1_account(json=json, status_code=201)
    time.sleep(3)

    token = mailhog.get_token_from_last_email()
    response = api.account.put_v1_account_token(token=token, status_code=200)

    assert_that(response.resource, has_properties(
        {
            "login": "login_Loginov192",
            "rating": [Rating.enabled, Rating.quality, Rating.quantity],
            "roles": [UserRole.GUEST, UserRole.PLAYER]
        }
    ))
