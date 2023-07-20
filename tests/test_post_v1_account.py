import time
from generic.helpers.orm_db import OrmDatabase
from services.dm_api_account import Facade
import structlog

structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False)
    ]
)


def test_post_v1_account():
    api = Facade(host="http://localhost:5051")
    login = "Login_41"
    email = "Login_41@email.ru"
    password = "qwerty12345"
    db = OrmDatabase(user='postgres', password='admin', host='localhost:5432', database='dm3.5')

    db.delete_user_by_login(login=login)
    dataset = db.get_users_by_login(login=login)
    assert len(dataset) == 0

    api.mailhog.delete_all_messages()

    api.account.register_new_user(
        login=login,
        email=email,
        password=password
    )

    dataset = db.get_users_by_login(login=login)
    for row in dataset:
        assert row['Login'] == login, f'User {login} not registered'
        assert row['Activated'] is False, f'User {login} was activated'

    # api.account.activate_registered_user(login=login)
    db.activate_user_by_login(login=login)

    time.sleep(3)

    dataset = db.get_users_by_login(login=login)
    for row in dataset:
        assert row['Activated'] is True, f'User {login} not activated'

    token = api.login.get_auth_token(login=login, password=password)
    api.account.set_headers(headers=token)
    api.account.get_current_user_info()
