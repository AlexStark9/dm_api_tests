def test_get_v1_account(dm_api_facade):
    token = dm_api_facade.login.get_auth_token(login="Login_616211", password="qwerty12345")
    dm_api_facade.account.set_headers(headers=token)
    dm_api_facade.account.get_current_user_info()
    print(token['X-Dm-Auth-Token'])
