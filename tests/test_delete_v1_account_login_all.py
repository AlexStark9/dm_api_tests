import allure


@allure.suite("Тесты на проверку метода DELETE{host}/v1/account")
@allure.sub_suite("Позитивные проверки")
@allure.title("Проверка выхода из системы со всех устройств")
def test_delete_v1_account_login_all(dm_api_facade, prepare_user, status_code=201):
    login = prepare_user.login
    email = prepare_user.email
    password = prepare_user.password

    dm_api_facade.account.register_new_user(
        login=login,
        email=email,
        password=password,
        status_code=status_code
    )

    dm_api_facade.account.activate_registered_user(login=login)

    token = dm_api_facade.login.get_auth_token(login=login, password=password)
    dm_api_facade.login.set_headers(headers=token)
    dm_api_facade.login.logout_user_from_all_devices()
