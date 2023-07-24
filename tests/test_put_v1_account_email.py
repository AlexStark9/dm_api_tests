from dm_api_account.models import ChangeEmail


def test_put_v1_account_email(dm_api_facade, prepare_user, status_code=201):
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

    json = ChangeEmail(
        login=login,
        email="User_Test6@mail.ru",
        password=password
    )

    response = dm_api_facade.account_api.put_v1_account_email(json=json)

    # assert_that(response.resource, has_properties(
    #     {
    #         "login": login,
    #         "roles": [UserRole.GUEST, UserRole.PLAYER],
    #         "rating": [Rating.enabled, Rating.quality, Rating.quantity]
    #     }
    # ))
