def test_put_v1_account_token(dm_api_facade, prepare_user, status_code=201):
    login = prepare_user.login
    email = prepare_user.email
    password = prepare_user.password

    dm_api_facade.account.register_new_user(
        login=login,
        email=email,
        password=password,
        status_code=status_code
    )

    response = dm_api_facade.account.activate_registered_user(login=login)

    # assert_that(response.resource, has_properties(
    #     {
    #         "login": login,
    #         "rating": [Rating.enabled, Rating.quality, Rating.quantity],
    #         "roles": [UserRole.GUEST, UserRole.PLAYER]
    #     }
    # ))
