import allure
import structlog

structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False)
    ]
)


@allure.suite("Тесты на проверку метода POST{host}/v1/account")
@allure.sub_suite("Позитивные проверки")
@allure.title("Проверка сброса пароля")
def test_post_v1_account_password(dm_api_facade, prepare_user, status_code=201):
    login = prepare_user.login
    email = prepare_user.email
    password = prepare_user.password

    dm_api_facade.account.register_new_user(
        login=login,
        email=email,
        password=password
    )

    dm_api_facade.account.activate_registered_user(login=login)
    token = dm_api_facade.login.get_auth_token(login=login, password=password)
    dm_api_facade.account.reset_password(
        x_dm_auth_token=token,
        login=login,
        email=email
    )
