from typing import List
import allure
from sqlalchemy import select, delete, update
from generic.helpers.orm_models import User
from common_libs.orm_client.orm_client import OrmClient


class OrmDatabase:
    def __init__(self, user, password, host, database):
        self.db = OrmClient(user, password, host, database)

    def get_all_users(self):
        """
        Get all users
        :return:
        """
        with allure.step("Получаем всех пользователей"):
            query = select(User)
            dataset = self.db.send_query(query)
            return dataset

    def get_users_by_login(self, login: str) -> List[User]:
        """
        Get user by logi
        :param login: str
        :return:
        """
        with allure.step("Получаем пользователя по логину"):
            query = select(User).where(
                User.Login == login
            )
            dataset = self.db.send_query(query)
            return dataset

    def delete_user_by_login(self, login: str):
        """
        Delete user by login
        :param login: str
        :return:
        """
        with allure.step("Разлогиниваем пользователя по логину"):
            query = delete(User).where(User.Login == login)
            dataset = self.db.send_bulk_query(query=query)
            return dataset

    def activate_user_by_login(self, login):
        """
        Activate user by login
        :param login: str
        :return:
        """
        with allure.step("Активируем пользователя по логину через db"):
            query = update(User).values({User.Activated: True}).where(User.Login == login)
            dataset = self.db.send_bulk_query(query=query)
            return dataset
