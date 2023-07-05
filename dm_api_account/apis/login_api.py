from requests import Response
from requests import session
from ..models.login_credentials_model import LoginCredentials
from rest_client.rest_client import Restclient
from dm_api_account.models.user_envelope import UserEnvelope


class LoginApi:
    def __init__(self, host, headers=None):
        self.host = host
        self.client = Restclient(host=host, headers=headers)
        if headers:
            self.client.session.headers.update(headers)

    def post_v1_account_login(self, json: LoginCredentials, **kwargs) -> Response:
        """
        Authenticate via credentials
        :param json: login_credentials_model
        :return:
        """

        response = self.client.post(
            path=f"/v1/account/login",
            json=json.dict(by_alias=True, exclude_none=True),
            **kwargs
        )

        return response

    def delete_v1_account_login(self, **kwargs) -> Response:
        """
        Logout as current user
        :return:
        """

        response = self.client.delete(
            path=f"/v1/account/login",
            **kwargs
        )
        UserEnvelope(**response.json())
        return response

    def delete_v1_account_login_all(self, **kwargs) -> Response:
        """
        Logout from every device
        :return:
        """

        response = self.client.delete(
            path=f"/v1/account/login/all",
            **kwargs
        )

        return response
