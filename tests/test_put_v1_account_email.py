from services.dm_api_account import DmApiAccount


def test_put_v1_account_email():
    api = DmApiAccount(host="http://localhost:5051")
    json = {
        "login": "User_9",
        "email": "User_9@mail.ru",
        "password": "qwerty12345"
    }

    response = api.account.put_v1_account_email(
        json=json
    )

    print(response)
