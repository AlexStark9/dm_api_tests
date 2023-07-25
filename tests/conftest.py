from collections import namedtuple
import random
from string import ascii_letters, digits
import pytest
from generic.helpers.orm_db import OrmDatabase
from services.dm_api_account import Facade
import structlog
from generic.helpers.mailhog import MailhogApi

structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False)
    ]
)


@pytest.fixture
def generating_test_data(begin: int = 6, end: int = 30):
    data = []
    symbols = ascii_letters + digits
    for i in range(3):
        string = ''
        for _ in range(random.randint(begin, end)):
            string += random.choice(symbols)
        if i == 1:
            data.append(string + '@mail.com')
        else:
            data.append(string)

    user = namedtuple('Data', 'login, email, password')
    Data = user(login=data[0], email=data[1], password=data[2])

    return Data


@pytest.fixture
def generating_invalid_test_data():
    login = ''
    email = ''
    password = ''
    symbols = ascii_letters + digits
    for _ in range(random.randint(1, 1)):
        login += random.choice(symbols)
    for _ in range(random.randint(1, 10)):
        email = email + random.choice(symbols) + 'mail.com'
    for _ in range(random.randint(1, 5)):
        login += random.choice(symbols)

    user = namedtuple('Data', 'login, email, password')
    Data = user(login=login, email=email, password=password)
    return Data


@pytest.fixture
def mailhog():
    return MailhogApi(host='http://5.63.153.31:5025')


@pytest.fixture
def dm_api_facade(mailhog):
    return Facade(host="http://5.63.153.31:5051", mailhog=mailhog)


@pytest.fixture
def dm_db():
    db = OrmDatabase(user='postgres', password='admin', host='5.63.153.31:5432', database='dm3.5')
    return db


@pytest.fixture
def prepare_user(dm_api_facade, dm_db, generating_test_data):
    user = namedtuple('User', 'login, email, password')
    User = user(
        login=generating_test_data.login,
        email=generating_test_data.email,
        password=generating_test_data.password
    )
    dm_db.delete_user_by_login(login=User.login)
    dataset = dm_db.get_users_by_login(login=User.login)
    assert len(dataset) == 0

    dm_api_facade.mailhog.delete_all_messages()

    return User


@pytest.fixture
def random_string(begin, end):
    symbol = ascii_letters + digits
    string = ''
    for _ in range(random.randint(begin, end)):
        string += random.choice(symbol)
    return string
