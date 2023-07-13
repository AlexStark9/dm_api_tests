from requests import Response
from services.dm_api_account import Facade
import structlog

structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False)
    ]
)


def test_get_v1_account():
    api = Facade(host="http://localhost:5051")
    token = api.login.get_auth_token(login="Login_32", password="qwerty12345")
    api.account.set_headers(headers=token)
    api.account.get_current_user_info()
