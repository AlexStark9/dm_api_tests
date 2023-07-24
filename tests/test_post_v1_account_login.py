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

    dm_api_facade.login.login_user(
        login=login,
        password=password
    )

    # assert_that(response.resource, has_properties(
    #     {
    #         "login": login,
    #         "roles": [UserRole.GUEST],
    #         "rating": [Rating.enabled, Rating.quality, Rating.quantity]
    #     }
    # ))
