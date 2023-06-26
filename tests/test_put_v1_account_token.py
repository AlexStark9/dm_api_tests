from services.dm_api_account import DmApiAccount


def test_put_v1_account_token():
    api = DmApiAccount(host="http://localhost:5051")

    response = api.account.put_v1_account_token(token="9370425b-5365-4dde-aeed-4339435e4360")

    print(response)
