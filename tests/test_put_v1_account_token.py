import time

from services.dm_api_account import DmApiAccount
from services.mailhog import MailhogApi
import structlog
from dm_api_account.models.registration_model import RegistrationModel

structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False)
    ]
)


def test_put_v1_account_token():
    mailhog = MailhogApi(host="http://localhost:5025")
    api = DmApiAccount(host="http://localhost:5051")
    json = RegistrationModel(
        login="login",
        email="User_Test11111@mail.ru",
        password="qwerty12345"
    )

    response = api.account.post_v1_account(json=json)
    assert response.status_code == 201, f'Статус код равен {response.status_code}, а должен быть равен 201!'
    time.sleep(2)
    token = mailhog.get_token_from_last_email
    response = api.account.put_v1_account_token(token=token)
