import allure
from dm_api_account.models import *


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

    def register_new_user(self, login: str, email: str, password: str, **kwargs):
        """
        Register new user
        :param login: str
        :param email: str
        :param password: str
        :return: response
        """
        with allure.step("Регистрация нового пользователя"):
            response = self.facade.account_api.register(
                **kwargs,
                registration=Registration(
                    login=login,
                    email=email,
                    password=password
                ))

        return response

    def activate_registered_user(self, login: str):
        """
        Activate registered user
        :param login: str
        :return: response
        """
        with allure.step("Активация зарегестрированного пользователя"):
            token = self.facade.mailhog.get_token_by_login(login=login)
            response = self.facade.account_api.activate(
                token=token
            )

        return response

    def get_current_user_info(self, x_dm_auth_token: str, **kwargs):
        """
        Get current user info
        :param x_dm_auth_token: str
        :param kwargs:
        :return:
        """
        with allure.step("Вывод информации о пользователе"):
            response = self.facade.account_api.get_current(x_dm_auth_token=x_dm_auth_token, **kwargs)
            return response

    def change_password(self, login: str, password: str, new_password: str, x_dm_auth_token: str):
        """
        Change password for registered user
        :param x_dm_auth_token: str
        :param new_password: str
        :param login: str
        :param password: str
        :return:
        """
        token = self.facade.mailhog.get_token_for_change_password(login)
        with allure.step("Меняем пароль от учетной записи пользователя"):
            response = self.facade.account_api.change_password(
                x_dm_auth_token=x_dm_auth_token,
                change_password=ChangePassword(
                    login=login,
                    token=token,
                    old_password=password,
                    new_password=new_password,
                )
            )

        return response

    def reset_password(self, login: str, email: str, x_dm_auth_token: str):
        """
        Reset password for change password
        :param x_dm_auth_token: str
        :param email: string
        :param login: str
        :return:
        """
        with allure.step("Сбрасываем пароль от учетной записи пользователя"):
            response = self.facade.account_api.reset_password(
                x_dm_auth_token=x_dm_auth_token,
                reset_password=ResetPassword(
                    login=login,
                    email=email
                )
            )
            return response

