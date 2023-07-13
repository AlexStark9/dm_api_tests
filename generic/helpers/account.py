from dm_api_account.models import Registration


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

    def register_new_user(self, login: str, email: str, password: str):
        """
        Register new user
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
            )
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
        response = self.facade.account_api.get_v1_account(**kwargs)
        return response
