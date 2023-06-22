import requests


def post_v1_account():
    """
    Register new user
    :return:
    """
    url = "http://localhost:5051/v1/account"

    payload = {
        "login": "User_3",
        "email": "User_3@mail.ru",
        "password": "qwerty12345"
    }
    headers = {
        'X-Dm-Auth-Token': '<string>',
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


response = post_v1_account()
print(response.request, response.content, response.url, response.status_code, response.json()['type'],
      response.json()['title'], sep="\n")
