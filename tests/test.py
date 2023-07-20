import structlog
from generic.helpers.orm_db import OrmDatabase
from generic.helpers.orm_models import User

structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False)
    ]
)


def test_orm():
    user = 'postgres'
    password = 'admin'
    host = 'localhost:5432'
    database = 'dm3.5'
    orm = OrmDatabase(user=user, password=password, host=host, database=database)

    dataset = orm.get_users_by_login(login='User_9')
    row: User
    for row in dataset:
        print(row.Name)
        print(row.Login)
        print(row.Email)

    orm.db.close_connection()
