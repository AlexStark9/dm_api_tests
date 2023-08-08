import allure

from apis.dm_api_account.models import *


class Account:
    def __init__(self, facade):
        from services.dm_api_account import Facade
        self.facade: Facade = facade

    def set_headers(self, headers):
        """
        Adding a title to the helper
        :param headers: kwargs
        :return:
        """
        self.facade.account_api.client.session.headers.update(headers)

    def register_new_user(self, login: str, email: str, password: str, status_code: int):
        """
        Register new user
        :param status_code: int
        :param login: str
        :param email: str
        :param password: str
        :return: response
        """
        response = self.facade.account_api.post_v1_account(
            json=Registration(
                login=login,
                email=email,
                password=password
            ),
            status_code=status_code
        )

        return response

    def activate_registered_user(self, login: str):
        """
        Activate registered user
        :param login: str
        :return: response
        """
        token = self.facade.mailhog.get_token_by_login(login=login)
        response = self.facade.account_api.put_v1_account_token(
            token=token
        )

        return response

    def get_current_user_info(self, **kwargs):
        """
        Get current user info
        :param kwargs:
        :return:
        """
        with allure.step("Вывод информации о пользователе"):
            response = self.facade.account_api.get_v1_account(**kwargs)
            return response

    def change_password(self, login: str, password: str, new_password: str, **kwargs):
        """
        Change password for registered user
        :param new_password: str
        :param login: str
        :param password: str
        :return:
        """
        token = self.facade.mailhog.get_token_for_change_password(login)

        response = self.facade.account_api.put_v1_account_password(
            json=ChangePassword(
                login=login,
                token=token,
                oldPassword=password,
                newPassword=new_password,
            )
        )

        return response

    def reset_password(self, login: str, email: str):
        """
        Reset password for change password
        :param email: string
        :param login: str
        :return:
        """
        response = self.facade.account_api.post_v1_account_password(
            json=ResetPassword(
                login=login,
                email=email
            )
        )

        return response
