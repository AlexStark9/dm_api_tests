import allure
from hamcrest import assert_that, has_properties
from dm_api_account.models.user_envelope import UserRole, Rating
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
        password=password,
        status_code=status_code
    )

    dm_api_facade.account.activate_registered_user(login=login)

    response = dm_api_facade.account.reset_password(
        login=login,
        email=email
    )
    # print(json.loads(response.json(by_alias=True, exclude_none=True)))
    assert_that(response.resource, has_properties(
        {
            "login": login,
            "rating": Rating(
                enabled=True,
                quality=0,
                quantity=0
            ),
            "roles": [UserRole.GUEST, UserRole.PLAYER]
        }
    ))
