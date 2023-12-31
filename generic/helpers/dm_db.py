import allure

from common_libs.db_client import DbClient


class DmDatabase:
    def __init__(self, user, password, host, database):
        self.db = DbClient(user, password, host, database)

    def get_all_users(self):
        with allure.step("Получаем всех пользователей"):
            query = 'select * from "public"."Users"'
            dataset = self.db.send_query(query=query)
            return dataset

    def get_user_by_login(self, login: str):
        with allure.step("Получаем пользователя по логину"):
            query = f'''
            select * from "public"."Users"
            where "Login" = '{login}'
            '''
            dataset = self.db.send_query(query=query)
            return dataset

    def delete_user_by_login(self, login: str):
        with allure.step("Разлогиниваем пользователя по логину"):
            query = f'''
            delete from "public"."Users"
            where "Login" = '{login}'
            '''
            dataset = self.db.send_bulk_query(query=query)
            return dataset

    def activate_user_by_login(self, login):
        with allure.step("Активируем пользователя по логину через db"):
            print('after start returning')
            query = f'''
            update "public"."Users"
            set "Activated" = true
            where "Login" = '{login}'
            '''
            dataset = self.db.send_bulk_query(query=query)
            return dataset
