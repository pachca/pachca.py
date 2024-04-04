from tests.fixtures.common import TEST_ID
from tests.fixtures.users import (EXPECT_RESPONSE_DATA_USER,
                                  EXPECT_RESPONSE_DATA_USERS)

from tests.test_base_client import TestBaseClient


class TestUsers(TestBaseClient):
    """Тестирует запросы бота к ресурсу 'users/'."""

    async def test_get_users_correct_data(self) -> None:
        """Тестирует метод 'get_users'.

        Проверяет корректность возвращаемых данных
        (список объектов пользователей, содержащиеся в массиве 'data')
        при безошибочном выполении ботом метода 'get_users'.
        """
        self.mock.return_value = EXPECT_RESPONSE_DATA_USERS
        response = await self.bot.get_users()
        self.assertEqual(
            response,
            EXPECT_RESPONSE_DATA_USERS,
            "При безошибочном выполении ботом метода 'get_users' "
            "возвращается список объектов пользователей."
        )

    async def test_get_user_correct_data(self) -> None:
        """Тестирует метод 'get_user'.

        Проверяет корректность возвращаемых данных
        (объект пользователя, содержащийся в массиве 'data')
        при безошибочном выполении ботом метода 'get_user'.
        """
        self.mock.return_value = EXPECT_RESPONSE_DATA_USER
        response = await self.bot.get_user(id=TEST_ID)
        self.assertEqual(
            response,
            EXPECT_RESPONSE_DATA_USER,
            "При безошибочном выполении ботом метода 'get_user' "
            "возвращается объектпользователя с указанным id "
        )
