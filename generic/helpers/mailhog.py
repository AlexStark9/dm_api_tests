import json
import time
import allure
from requests import Response
from common_libs.rest_client.rest_client import Restclient


# def decorator(fn):
#     def wrapper(*args, **kwargs):
#         for i in range(5):
#             response = fn(*args, **kwargs)
#             emails = response.json()['items']
#             if len(emails) < 5:
#                 time.sleep(3)
#                 continue
#             else:
#                 return response
#
#     return wrapper


class MailhogApi:
    def __init__(self, host):
        self.host = host
        self.client = Restclient(host=host)

    def get_api_v2_messages(self, limit: int = 50) -> Response:
        """
        Get messages by limit
        :param limit: int
        :return:
        """
        with allure.step(f"Получаем {limit} сообщений с почты"):
            response = self.client.get(
                path=f"/api/v2/messages",
                params={
                    'limit': limit
                }
            )

        return response

    def get_token_from_last_email(self) -> str:
        """
        Get user activation token from last email
        :return: token
        """
        with allure.step("Получаем токен в последнем сообщении"):
            email = self.get_api_v2_messages(limit=1).json()
            token_url = json.loads(email['items'][0]['Content']['Body'])['ConfirmationLinkUri']
            token = token_url.split('/')[-1]
            return token

    def get_token_by_login(self, login: str, attempt=5):
        """
        Get user activation token using login
        :param login: str
        :param attempt: int
        :return: token
        """
        with allure.step("Получаем токен для автризации пользователя"):
            if attempt == 0:
                raise AssertionError(f'Не удалось получить письмо с логином {login}')
            emails = self.get_api_v2_messages(limit=100).json()['items']
            for email in emails:
                user_data = json.loads(email['Content']['Body'])
                if login == user_data.get('Login'):
                    token = user_data['ConfirmationLinkUrl'].split('/')[-1]
                    return token
            time.sleep(3)
            attempt -= 1
            return self.get_token_by_login(login=login, attempt=attempt - 1)

    def get_token_for_change_password(self, login: str, attempt=5):
        """
        Get token for change password
        :param login: str
        :param attempt: int
        :return: token
        """
        with allure.step("Получаем токен для смены пароля"):
            if attempt == 0:
                raise AssertionError(f'Не удалось получить письмо с логином {login}')
            emails = self.get_api_v2_messages(limit=100).json()['items']
            for email in emails:
                user_data = json.loads(email['Content']['Body'])
                if login == user_data.get('Login'):
                    token = user_data['ConfirmationLinkUri'].split('/')[-1]
                    return token
            time.sleep(3)
            attempt -= 1
            return self.get_token_for_change_password(login=login, attempt=attempt - 1)

    def delete_all_messages(self):
        with allure.step("Удаляем все сообщения"):
            response = self.client.delete(path='/api/v1/messages')
            return response
