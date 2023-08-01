import time
import allure


@allure.suite("Тесты на проверку метода GET{host}/v1/account")
@allure.sub_suite("Позитивные проверки")
@allure.title("Проверка вывода информации о пользователе")
def test_get_v1_account(dm_api_facade, prepare_user, dm_db, status_code=201):
    login = prepare_user.login
    password = prepare_user.password
    email = prepare_user.email

    dm_api_facade.account.register_new_user(
        login=login,
        email=email,
        password=password,
        status_code=status_code
    )
    dm_db.activate_user_by_login(login=login)
    time.sleep(3)

    token = dm_api_facade.login.get_auth_token(login, password)
    dm_api_facade.account.set_headers(headers=token)
    dm_api_facade.account.get_current_user_info()
    print(token['X-Dm-Auth-Token'])
