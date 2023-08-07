import allure


@allure.suite("Тесты на проверку метода POST{host}/v1/account")
@allure.sub_suite("Позитивные проверки")
@allure.title("Проверка авторизации пользователя")
def test_post_v1_account_login(dm_api_facade, prepare_user, status_code=201):
    """
    Authenticate via credentials
    :return:
    """
    login = prepare_user.login
    email = prepare_user.email
    password = prepare_user.password

    dm_api_facade.account.register_new_user(
        login=login,
        email=email,
        password=password
    )

    dm_api_facade.account.activate_registered_user(login=login)

    response = dm_api_facade.login.login_user(
        login=login,
        password=password
    )

