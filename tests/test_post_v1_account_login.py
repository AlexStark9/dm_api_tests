from hamcrest import assert_that, has_properties
from dm_api_account.models.user_envelope import UserRole, Rating


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
        password=password,
        status_code=status_code
    )

    dm_api_facade.account.activate_registered_user(login=login)

    response = dm_api_facade.login.login_user(
        login=login,
        password=password
    )
    # Для метода post_v1_account_login возвращаем json
    # assert_that(response.resource, has_properties(
    #     {
    #         "login": login,
    #         "rating": Rating(
    #             enabled=True,
    #             quality=0,
    #             quantity=0
    #         ),
    #         "roles": [UserRole.GUEST, UserRole.PLAYER]
    #     }
    # ))
