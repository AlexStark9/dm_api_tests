import time


def test_put_v1_account_password(dm_api_facade, prepare_user, status_code=201):
    login = prepare_user.login
    email = prepare_user.email
    password = prepare_user.password
    new_password = 'qwerty12345'

    dm_api_facade.account.register_new_user(
        login=login,
        email=email,
        password=password,
        status_code=status_code
    )

    dm_api_facade.account.activate_registered_user(login=login)

    token = dm_api_facade.login.get_auth_token(
        login=login,
        password=password
    )
    dm_api_facade.account.set_headers(headers=token)

    dm_api_facade.account.reset_password(
        login=login,
        email=email
    )
    time.sleep(3)

    dm_api_facade.account.change_password(
        login=login,
        password=password,
        new_password=new_password
    )

    # assert_that(response.resource, has_properties(
    #     {
    #         "login": login,
    #         "roles": [UserRole.GUEST, UserRole.PLAYER],
    #         "rating": [Rating.enabled, Rating.quality, Rating.quantity]
    #     }
    # ))
