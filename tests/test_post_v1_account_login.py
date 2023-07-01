import requests
import time

from services.dm_api_account import DmApiAccount
from services.mailhog import MailhogApi
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
    mailhog = MailhogApi(host="http://localhost:5025")
    api = DmApiAccount(host="http://localhost:5051")
    json = {
        "login": "User_Test111",
        "email": "User_Test111@mail.ru",
        "password": "qwerty12345"
    }

    response = api.account.post_v1_account(json=json)
    assert response.status_code == 201, f'Статус код равен {response.status_code}, а должен быть равен 201!'
    time.sleep(2)
    token = mailhog.get_token_from_last_email
    response = api.account.put_v1_account_token(token=token)

    api = DmApiAccount(host="http://localhost:5051")

    json = {
        "login": "User_Test111",
        "password": "qwerty12345",
        "rememberMe": "<boolean>"
    }

    response = api.login.post_v1_account_login(json=json)
