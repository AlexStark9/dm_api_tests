import time
from dm_api_account.models.registration_model import Registration
from services.dm_api_account import DmApiAccount
from services.mailhog import MailhogApi
import structlog
from dm_api_account.models.change_password_model import ChangePassword
import json

structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False)
    ]
)


def test_put_v1_account_password():
    login = 'Login777'
    password = 'password'

    mailhog = MailhogApi(host="http://localhost:5025")
    api = DmApiAccount(host="http://localhost:5051")
    # body = Registration(
    #     login=login,
    #     email="User_777@mail.ru",
    #     password=password
    # )
    #
    # response = api.account.post_v1_account(json=body, status_code=201)

    # time.sleep(3)
    token = mailhog.get_token_from_last_email()
    # response = api.account.put_v1_account_token(token=token, status_code=200)
    body = ChangePassword(
        login=login,
        token=token,
        oldPassword=password,
        newPassword='qwerty12345'
    )

    response = api.account.put_v1_account_password(json=body)
    print(json.loads(response.json(by_alias=True, exclude_none=True)))
