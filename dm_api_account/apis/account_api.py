import allure
from requests import Response
from ..models import *
from rest_client.rest_client import Restclient
from dm_api_account.utilities import validate_request_json, validate_status_code


class AccountApi:
    def __init__(self, host, headers=None):
        self.host = host
        self.client = Restclient(host=host, headers=headers)
        if headers:
            self.client.session.headers.update(headers)

    def post_v1_account(self, json: Registration, status_code: int,
                        **kwargs) -> BadRequestError | Response:
        """
        Register new user
        :param status_code: int
        :param json registration_model
        :return:
        """
        with allure.step("Регистрация нового пользователя"):
            response = self.client.post(
                path=f"/v1/account",
                json=validate_request_json(json),
                **kwargs
            )

        validate_status_code(response, status_code)
        # if response.status_code == 400:
        #     return BadRequestError(**response.json())
        #
        return response

    def post_v1_account_password(self, json: ResetPassword, status_code: int = 200,
                                 **kwargs) -> UserEnvelope | BadRequestError | Response:
        """
        Reset registered user password
        :param status_code: int
        :param json reset_password_model
        :return:
        """

        response = self.client.post(
            path=f"/v1/account/password",
            json=validate_request_json(json),
            **kwargs
        )

        validate_status_code(response, status_code)
        if response.status_code == 200:
            return UserEnvelope(**response.json())
        # elif response.status_code == 400:
        #     return BadRequestError(**response.json())
        # else:
        # return response

    def put_v1_account_email(self, json: ChangeEmail, status_code: int = 200,
                             **kwargs) -> UserEnvelope | BadRequestError | Response:
        """
        Change registered user email
        :param status_code: int
        :param json change_email_model
        :return:
        """

        response = self.client.put(
            path=f"/v1/account/email",
            json=validate_request_json(json),
            **kwargs
        )

        validate_status_code(response, status_code)
        if response.status_code == status_code:
            return UserEnvelope(**response.json())
        # elif response.status_code == 400:
        #     return BadRequestError(**response.json())
        # else:
        return response

    def put_v1_account_password(self, json: ChangePassword, status_code: int = 200,
                                **kwargs) -> UserEnvelope | BadRequestError | Response:
        """
        Change registered user password
        :param status_code: int
        :param json change_password_model
        :return:
        """

        response = self.client.put(
            path=f"/v1/account/password",
            json=validate_request_json(json),
            **kwargs
        )

        validate_status_code(response, status_code)
        if response.status_code == status_code:
            return UserEnvelope(**response.json())
        # elif response.status_code == 400:
        #     return BadRequestError(**response.json())
        # else:
        # return response

    def put_v1_account_token(self, token: str, status_code: int = 200,
                             **kwargs) -> UserEnvelope | GeneralError | Response:
        """
        Activate registered user
        :param status_code: int
        :param token: str
        :return:
        """
        with allure.step("Регистрация нового пользователя"):
            response = self.client.put(
                path=f"/v1/account/{token}",
                **kwargs
            )

        validate_status_code(response, status_code)
        if response.status_code == status_code:
            return UserEnvelope(**response.json())
        # elif response.status_code == 400:
        #     return GeneralError(**response.json())
        # elif response.status_code == 410:
        #     return GeneralError(**response.json())
        # else:
        # return response

    def get_v1_account(self, status_code: int = 200, **kwargs) -> Response | UserDetailsEnvelope:
        """
        Get current user
        :return:
        """

        response = self.client.get(
            path=f"/v1/account",
            **kwargs
        )
        validate_status_code(response, status_code)
        if response.status_code == status_code:
            return UserDetailsEnvelope(**response.json())
        # else:
        # return response
