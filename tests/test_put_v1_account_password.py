import time

from services.dm_api_account import DmApiAccount
from services.mailhog import MailhogApi
import structlog
from dm_api_account.models.change_password_model import ChangePassword

structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False)
    ]
)


def test_put_v1_account_password():
    mailhog = MailhogApi(host="http://localhost:5025")
    api = DmApiAccount(host="http://localhost:5051")
    json = ChangePassword(
        login='',
        token='',
        oldPassword='',
        newPassword=''
    )

    response = api.account.post_v1_account(json=json)
    assert response.status_code == 201, f'Статус код равен {response.status_code}, а должен быть равен 201!'
    time.sleep(2)
    token = mailhog.get_token_from_last_email
    response = api.account.put_v1_account_token(token=token)
    json = {
        "login": "User_4",
        "token": "129dbf2c-a964-47cf-96e4-590938c77579",
        "oldPassword": "qwerty12345",
        "newPassword": "12345qwerty"
    }

    response = api.account.put_v1_account_password(json=json)
