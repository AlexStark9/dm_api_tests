import requests


class LoginApi:
    def __int__(self):
        ...

    def post_v1_account_login(self):
        """
        Authenticate via credentials
        :return:
        """
        url = "http://localhost:5051/v1/account/login"

        payload = {
            "login": "<string>",
            "password": "<string>",
            "rememberMe": "<boolean>"
        }
        headers = {
            'X-Dm-Bb-Render-Mode': '<string>',
            'Content-Type': 'application/json',
            'Accept': 'text/plain'
        }

        response = requests.request(
            method="POST",
            url=url,
            headers=headers,
            json=payload
        )

        return response

    def delete_v1_account_login(self):
        """
        Logout as current user
        :return:
        """
        url = "http://localhost:5051/v1/account/login"

        headers = {
            'X-Dm-Auth-Token': '<string>',
            'X-Dm-Bb-Render-Mode': '<string>',
            'Accept': 'text/plain'
        }

        response = requests.request(
            method="DELETE",
            url=url,
            headers=headers
        )

        return response

    def delete_v1_account_login_all(self):
        """
        Logout from every device
        :return:
        """
        url = "http://localhost:5051/v1/account/login/all"

        headers = {
            'X-Dm-Auth-Token': '<string>',
            'X-Dm-Bb-Render-Mode': '<string>',
            'Accept': 'text/plain'
        }

        response = requests.request(
            method="DELETE",
            url=url,
            headers=headers
        )

        return response
