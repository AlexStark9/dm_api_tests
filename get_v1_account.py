import requests


def get_v1_account():
    """
    Get current user
    :return:
    """
    url = "http://localhost:5051/v1/account"

    headers = {
        'X-Dm-Auth-Token': '',
        'X-Dm-Bb-Render-Mode': '',
        'Accept': ''
    }

    response = requests.request(
        method="GET", url=url,
        headers=headers,
        json=payload
    )

    return response
