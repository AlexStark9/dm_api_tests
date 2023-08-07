import time
import allure


@allure.suite("Тесты на проверку метода PUT{host}/v1/account")
@allure.sub_suite("Позитивные проверки")
@allure.title("Проверка смены пароля")
def test_put_v1_account_password(dm_api_facade, prepare_user):
    login = prepare_user.login
    email = prepare_user.email
    password = prepare_user.password
    new_password = 'qwerty12345'

    dm_api_facade.account.register_new_user(
        login=login,
        email=email,
        password=password
    )

    dm_api_facade.account.activate_registered_user(login=login)
    token = dm_api_facade.login.get_auth_token(
        login=login,
        password=password
    )

    dm_api_facade.account.reset_password(
        x_dm_auth_token=token,
        login=login,
        email=email
    )
    time.sleep(3)

    dm_api_facade.account.change_password(
        login=login,
        password=password,
        new_password=new_password,
        x_dm_auth_token=token
    )
