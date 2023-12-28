from pydantic_core import ValidationError

from tests.fixtures.chats import (EXPECT_RESPONSE_DATA_CHAT,
                                  EXPECT_RESPONSE_DATA_CHATS,
                                  INCORRECT_CHAT_DATA, NEW_CHAT_DATA)
from tests.fixtures.common import EXPECT_RESPONSE_ERRORS, TEST_ID
from tests.test_base_client import TestBaseClient


class TestChats(TestBaseClient):
    """Тестирует запросы бота к ресурсу 'chats/'."""

    async def test_get_chats_correct_data(self) -> None:
        """Тестирует метод 'get_chats'.

        Проверяет корректность возвращаемых данных
        (список объектов бесед, содержащиеся в массиве 'data')
        при безошибочном выполении ботом метода 'get_chats'.
        """
        self.mock.return_value = EXPECT_RESPONSE_DATA_CHATS
        response = await self.bot.get_chats()
        self.assertEqual(
            response,
            EXPECT_RESPONSE_DATA_CHATS,
            "При безошибочном выполении ботом метода 'get_chats' "
            "возвращается список объектов пользователей."
        )

    async def test_get_chat_by_id_correct_data(self) -> None:
        """Тестирует метод 'get_chat_by_id'.

        Проверяет корректность возвращаемых данных
        (объект беседы, содержащийся в массиве 'data')
        при безошибочном выполении ботом метода 'get_chat_by_id'.
        """
        self.mock.return_value = EXPECT_RESPONSE_DATA_CHATS
        response = await self.bot.get_chat_by_id(TEST_ID)
        self.assertEqual(
            response,
            EXPECT_RESPONSE_DATA_CHATS,
            "При безошибочном выполении ботом метода 'get_chats_by_id' "
            "возвращается объект пользователя, "
            "id которого было передано в метод."
        )

    async def test_create_chat_correct_data(self) -> None:
        """Тестирует метод 'create_chat' c корректным телом запроса.

        Проверяет корректность возвращаемых данных
        (объект беседы, содержащийся в массиве 'data')
        при безошибочном выполении ботом метода 'create_chat'.
        """
        new_chat_data = NEW_CHAT_DATA
        self.mock.return_value = EXPECT_RESPONSE_DATA_CHAT
        response = await self.bot.create_chat(new_chat_data)
        self.assertEqual(
            response,
            EXPECT_RESPONSE_DATA_CHAT,
            'При создании новой беседы/канала '
            'возвращается информация о созданном объекте'
        )

    async def test_create_chat_incorrect_data(self) -> None:
        """Тестирует метод 'create_chat' c некорректным телом запроса.

        Проверяет корректность валидации данных на стороне клиента
        (возникновение ошибки ValidationError)
        при выполении ботом метода 'create_chat' с
        некорректными телом запроса.
        """
        new_chat_data = INCORRECT_CHAT_DATA
        self.mock.return_value = EXPECT_RESPONSE_ERRORS
        with self.assertRaises(
            ValidationError,
            msg=(
                "При выполнении метода 'create_chat' c некорректным "
                "телом запроса должна возникать ошибка ValidationError"
            )
        ):
            await self.bot.create_chat(new_chat_data)

    # async def test_update_chats_correct_data(self) -> None:
    #     """Тестирует метод 'put' c корректным телом запроса.

    #     Проверяет корректность возвращаемых данных
    #     (объект беседы, содержащийся в массиве 'data')
    #     при безошибочном выполении клиентом метода 'put'.
    #     """
    #     update_chat_data = UPDATE_CHAT_DATA
    #     self.mock.return_value = EXPECT_RESPONSE_DATA_CHAT
    #     response = await self.client.put(
    #         urljoin(self.chats_url, TEST_ID),
    #         update_chat_data
    #     )
    #     self.assertEqual(
    #         response,
    #         EXPECT_RESPONSE_DATA_CHAT,
    #         'При редактирование беседы/канала '
    #         'возвращается информация об обновленном объекте'
    #     )

    # async def test_update_chat_incorrect_data(self) -> None:
    #     """Тестирует метод 'put'c некорректным телом запроса.

    #     Проверяет корректность возвращаемых данных
    #     (опсание ошибки, содержащееся в массиве errors)
    #     при выполении клиентом метода 'put' с
    #     некорректными телом запроса.
    #     """
    #     new_chat_data = INCORRECT_CHAT_DATA
    #     self.mock.return_value = EXPECT_RESPONSE_ERRORS
    #     response = await self.client.put(
    #         urljoin(self.chats_url, TEST_ID),
    #         new_chat_data
    #     )
    #     self.assertEqual(
    #         response,
    #         EXPECT_RESPONSE_ERRORS,
    #         ERROR_ARRAY_MESSAGE
    #     )
