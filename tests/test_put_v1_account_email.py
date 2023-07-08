import time
from hamcrest import assert_that, has_properties
from dm_api_account.models.registration_model import Registration
from dm_api_account.models.user_envelope import UserRole, Rating
from services.dm_api_account import DmApiAccount
from services.mailhog import MailhogApi
import structlog
from dm_api_account.models.change_email_model import ChangeEmail

structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False)
    ]
)


def test_put_v1_account_email():
    login = 'Login_Tester6'
    password = 'password'

    mailhog = MailhogApi(host="http://localhost:5025")
    api = DmApiAccount(host="http://localhost:5051")
    json = Registration(
        login=login,
        email="User_Test6@mail.ru",
        password=password
    )

    response = api.account.post_v1_account(json=json, status_code=201)

    time.sleep(3)
    token = mailhog.get_token_from_last_email()
    response = api.account.put_v1_account_token(token=token, status_code=200)

    json = ChangeEmail(
        login=login,
        email="User_Test6@mail.ru",
        password=password
    )

    response = api.account.put_v1_account_email(json=json)
    # print(json.loads(response.json(by_alias=True, exclude_none=True)))
    assert_that(response.resource, has_properties(
        {
            "login": login,
            "roles": [UserRole.GUEST, UserRole.PLAYER],
            "rating": [Rating.enabled, Rating.quality, Rating.quantity]
        }
    ))
