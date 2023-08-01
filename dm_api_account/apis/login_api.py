import allure
from requests import Response
from rest_client.rest_client import Restclient
from ..models import *
from dm_api_account.utilities import validate_request_json, validate_status_code
from ..models import UserEnvelope, GeneralError, BadRequestError


class LoginApi:
    def __init__(self, host, headers=None):
        self.host = host
        self.client = Restclient(host=host, headers=headers)
        if headers:
            self.client.session.headers.update(headers)

    def post_v1_account_login(self, json: LoginCredentials,
                              status_code: int = 200, **kwargs) -> UserEnvelope | BadRequestError | GeneralError | Response:
        """
        Authenticate via credentials
        :param status_code: int
        :param json: login_credentials_model
        :return:
        """
        with allure.step("Authenticate via credentials"):
            response = self.client.post(
                path=f"/v1/account/login",
                json=validate_request_json(json)
            )

        validate_status_code(response, status_code)
        # if response.status_code == status_code:
        #     return UserEnvelope(**response.json())
        # elif response.status_code == 400:
        #     return BadRequestError(**response.json())
        # elif response.status_code == 403:
        #     return GeneralError(**response.json())
        # else:
        return response

    def delete_v1_account_login(self, status_code: int = 204,
                                **kwargs) -> GeneralError | Response:
        """
        Logout as current user
        :param status_code: int
        :return:
        """
        with allure.step("Logout as current user"):
            response = self.client.delete(
                path=f"/v1/account/login",
                **kwargs
            )

        validate_status_code(response, status_code)
        # if response.status_code == 401:
        #     return GeneralError(**response.json())
        # else:
        return response

    def delete_v1_account_login_all(self, status_code: int = 204,
                                    **kwargs) -> GeneralError | Response:
        """
        Logout from every device
        :param status_code: int
        :return:
        """
        with allure.step("Logout from every device"):
            response = self.client.delete(
                path=f"/v1/account/login/all",
                **kwargs
            )

        validate_status_code(response, status_code)
        # if response.status_code == 401:
        #     return GeneralError(**response.json())
        # else:
        return response
