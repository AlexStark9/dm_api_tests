import time

from services.dm_api_account import DmApiAccount
from services.mailhog import MailhogApi
import structlog
from dm_api_account.models.reset_password_model import ResetPassword

structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False)
    ]
)


def test_post_v1_account_password():
    mailhog = MailhogApi(host="http://localhost:5025")
    api = DmApiAccount(host="http://localhost:5051")
    json = ResetPassword(
        login="Login",
        email="User_Test1@mail.ru"
    )

    response = api.account.post_v1_account(json=json)
    assert response.status_code == 201, f'Статус код равен {response.status_code}, а должен быть равен 201!'
    time.sleep(2)
    token = mailhog.get_token_from_last_email
    response = api.account.put_v1_account_token(token=token)
    json = {
        "login": "User_Test_4",
        "email": "User_Test_4@mail.ru"
    }

    response = api.account.post_v1_account_password(json=json)
