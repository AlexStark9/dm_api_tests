import uuid
import allure
import records
import structlog

structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False)
    ]
)


def allure_attach(fn):
    def wrapper(*args, **kwargs):
        query = kwargs.get('query')
        allure.attach(str(query), name='SQL_query', attachment_type=allure.attachment_type.TEXT)
        dataset = fn(*args, **kwargs)
        if dataset is not None:
            allure.attach(str(dataset), name='dataset', attachment_type=allure.attachment_type.TEXT)
        return dataset

    return wrapper


class DbClient:
    def __init__(self, user, password, host, database, isolation_level='AUTOCOMMIT'):
        connection_string = f'postgresql://{user}:{password}@{host}/{database}'
        self.db = records.Database(connection_string, isolation_level=isolation_level)
        self.log = structlog.get_logger(self.__class__.__name__).bind(service='db')

    @allure_attach
    def send_query(self, query):
        print(query)
        log = self.log.bind(event_id=str(uuid.uuid4()))
        log.msg(
            event='request',
            query=query
        )
        dataset = self.db.query(query=query).as_dict()
        log.msg(
            event='response',
            dataset=dataset
        )
        return dataset

    @allure_attach
    def send_bulk_query(self, query):
        print(query)
        log = self.log.bind(event_id=str(uuid.uuid4()))
        log.msg(
            event='request',
            query=query
        )
        self.db.bulk_query(query=query)


if __name__ == "__main__":
    db = DbClient(user='postgres', password='admin', host='5.63.153.31:5432', database='dm3.5')
    query = 'select * from "public"."Users"'
    db.send_query(query)
