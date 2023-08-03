import allure

from dm_api_account.models import *


class Login:
    def __init__(self, facade):
        self.facade = facade

    def set_headers(self, headers):
        """
        Adding a title to the helper
        :param headers: kwargs
        :return:
        """
        self.facade.login_api.client.session.headers.update(headers)

    def login_user(self, login: str, password: str, remember_me: bool = True):
        """
        Login user
        :param login: str
        :param password: str
        :param remember_me: bool
        :return: response
        """
        with allure.step("Авторизация пользователя"):
            response = self.facade.login_api.post_v1_account_login(
                json=LoginCredentials(
                    login=login,
                    password=password,
                    remember_me=remember_me
                )
            )

        return response

    def get_auth_token(self, login: str, password: str, remember_me: bool = True):
        """
        Get auth token
        :param login: str
        :param password: str
        :param remember_me: bool
        :return:
        """
        with allure.step("Авторизация пользователя и получение авторизационного токена"):
            response = self.login_user(login=login, password=password, remember_me=remember_me)
            return {'X-Dm-Auth-Token': response.headers['X-Dm-Auth-Token']}

    def logout_user(self, **kwargs):
        """
        Logout user
        :param kwargs: kwargs
        :return:
        """
        return self.facade.login_api.delete_v1_account_login(**kwargs)

    def logout_user_from_all_devices(self, **kwargs):
        """
        Logout user from all devices
        :param kwargs: kwargs
        :return:
        """
        return self.facade.login_api.delete_v1_account_login_all(**kwargs)
