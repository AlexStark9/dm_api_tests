from services.dm_api_account import DmApiAccount


def test_put_v1_account_password():
    api = DmApiAccount(host="http://localhost:5051")
    json = {
        "login": "User_4",
        "token": "129dbf2c-a964-47cf-96e4-590938c77579",
        "oldPassword": "qwerty12345",
        "newPassword": "12345qwerty"
    }

    response = api.account.put_v1_account_password(
        json=json
    )

    print(response)
