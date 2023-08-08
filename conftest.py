import pytest
import random
import structlog
from vyper import v
from pathlib import Path
from string import ascii_letters, digits
from apis.dm_api_search_async import SearchEngineStub
from generic.assertions.post_v1_account import AssertionsPostV1Account
from generic.helpers.orm_db import OrmDatabase
from generic.helpers.search import Search
from services.dm_api_account import Facade
from collections import namedtuple
from generic.helpers.mailhog import MailhogApi
from grpclib.client import Channel


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
    return MailhogApi(host=v.get('service.mailhog'))


@pytest.fixture
def dm_api_facade(mailhog):
    return Facade(
        host=v.get('service.dm_api_account'),
        mailhog=mailhog
    )


@pytest.fixture()
def assertion(dm_db):
    return AssertionsPostV1Account(dm_db)


@pytest.fixture
def dm_db():
    db = OrmDatabase(
        user=v.get('database.dm3_5.user'),
        password=v.get('database.dm3_5.password'),
        host=v.get('database.dm3_5.host'),
        database=v.get('database.dm3_5.database')
    )
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


options = (
    'service.dm_api_account',
    'service.mailhog',
    'service.dm3_5.host'
)


@pytest.fixture(autouse=True)
def set_config(request):
    config = Path(__file__).parent.joinpath('config')
    print(config)
    config_name = request.config.getoption('--env')
    v.set_config_name(config_name)
    v.add_config_path(config)
    v.read_in_config()
    for option in options:
        v.set(option, request.config.getoption(f'--{option}'))


def pytest_addoption(parser):
    parser.addoption('--env', action='store', default='stg')
    for option in options:
        parser.addoption(f'--{option}', action='store', default=None)


@pytest.fixture
def grpc_search():
    client = Search(target=v.get('service.dm_api_search'))
    yield client
    client.grpc_search.close()


@pytest.fixture
def grpc_search_async():
    channel = Channel(host='5.63.153.31', port=5052)
    client = SearchEngineStub(channel)
    yield client
    channel.close()
