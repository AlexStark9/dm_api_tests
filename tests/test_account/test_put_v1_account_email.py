import allure
from dm_api_account.models import ChangeEmail


@allure.suite("Тесты на проверку метода PUT{host}/v1/account")
@allure.sub_suite("Позитивные проверки")
@allure.title("Проверка смены email")
def test_put_v1_account_email(dm_api_facade, prepare_user):
    login = prepare_user.login
    email = prepare_user.email
    password = prepare_user.password

    dm_api_facade.account.register_new_user(
        login=login,
        email=email,
        password=password
    )

    dm_api_facade.account.activate_registered_user(login=login)

    data = ChangeEmail(
        login=login,
        email="User_Test6@mail.ru",
        password=password
    )

    dm_api_facade.account_api.change_email(change_email=data)
