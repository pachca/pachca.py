from pydantic_core import ValidationError
from tests.fixtures.common import TEST_ID, EMPTY_ARRAY
from tests.fixtures.members_chats_channels import (PREPARE_CORRECT_MEMBERS,
                                                   PREPARE_CORRECT_TAGS,
                                                   PREPARE_INCORRECT_MEMBERS,
                                                   PREPARE_INCORRECT_TAGS)
from tests.test_base_client import TestBaseClient


class TestMembersInChatsAndChannelsTest(TestBaseClient):
    """Тестирует запросы бота к ресурсам '/chats/{id}/members',
    /chats/{id}/group_tags.
    """

    async def test_add_members_to_chat(self) -> None:
        """Тестирует метод 'post'.
        Добавление пользователей в состав участников беседы/канала.
        Добавление тегов в состав участников беседы/канала.

        Проверяет корректность возвращаемых данных
        (без тела ответа) при безошибочном выполнении
        клиентом метода 'post'.
        """
        self.mock.return_value = EMPTY_ARRAY
        response = await self.bot.add_members_to_chat(
            TEST_ID, PREPARE_CORRECT_MEMBERS
        )
        self.assertEqual(
            EMPTY_ARRAY,
            response,
            'При безошибочном выполнении запроса тело '
            'ответа отсутствует'
        )

    async def test_add_tags_to_chat(self) -> None:
        """Тестирует метод 'add_tags_to_chat'.
        Добавление пользователей в состав участников беседы/канала.
        Добавление тегов в состав участников беседы/канала.

        Проверяет корректность возвращаемых данных
        (без тела ответа) при безошибочном выполнении
        ботом метода 'add_tags_to_chat'.
        """
        self.mock.return_value = EMPTY_ARRAY
        response = await self.bot.add_tags_to_chat(
            TEST_ID, PREPARE_CORRECT_TAGS
        )
        self.assertEqual(
            EMPTY_ARRAY,
            response,
            'При безошибочном выполнении запроса тело '
            'ответа отсутствует'
        )

    async def test_add_members_to_chat_incorrect_data(self) -> None:
        """Тестирует метод 'add_members_to_chat'.
        Добавление пользователей в состав участников беседы/канала.
        Добавление тегов в состав участников беседы/канала.

        Проверяет корректность возвращаемых данных
        (возникновение ошибки ValidationError)
        при выполении ботом метода 'add_members_to_chat с
        некорректными телом запроса.
        """
        with self.assertRaises(
            ValidationError,
            msg=(
                "При выполнении метода 'add_members_to_chat' c некорректным "
                "телом запроса должна возникать ошибка ValidationError"
            )
        ):
            await self.bot.add_members_to_chat(
                TEST_ID, PREPARE_INCORRECT_MEMBERS
            )

    async def test_add_tags_to_chat_incorrect_data(self) -> None:
        """Тестирует метод 'add_tags_to_chat'.
        Добавление пользователей в состав участников беседы/канала.
        Добавление тегов в состав участников беседы/канала.

        Проверяет корректность возвращаемых данных
        (возникновение ошибки ValidationError)
        при выполении ботом метода 'add_tags_to_chat' с
        некорректными телом запроса.
        """
        with self.assertRaises(
            ValidationError,
            msg=(
                "При выполнении метода 'add_tags_to_chat' c некорректным "
                "телом запроса должна возникать ошибка ValidationError"
            )
        ):
            await self.bot.add_tags_to_chat(
                TEST_ID, PREPARE_INCORRECT_TAGS
            )

#     async def test_del_correct(self) -> None:
#         """Тестирует метод 'del'.
#         Исключение пользователя из состава участников беседы/канала.
#         Исключение тега из состава участников беседы/канала.

#         Проверяет корректность возвращаемых данных
#         (без тела ответа) при безошибочном выполнении
#         клиентом метода 'del'.
#         """
#         self.mock.return_value = self.prepare_response_correct_data
#         for url in self.url_del:
#             with self.subTest(url):
#                 response = await self.client.delete(url)
#                 self.assertEqual(
#                     self.prepare_response_correct_data,
#                     response,
#                     'При безошибочном выполнение запроса '
#                     'тело ответа отсутвует')

#     async def test_del_incorrect(self) -> None:
#         """Тестирует метод 'del'.
#         Исключение пользователя из состава участников беседы/канала.
#         Исключение тега из состава участников беседы/канала.

#         Проверяет корректность возвращаемых данных
#         (описание оишбки, содержащееся в массиве errors)
#         при выполении клиентом метода 'del' с
#         некорректными параметрами пути.
#         """
#         self.mock.return_value = self.prepare_response_errors
#         for url in self.url_del:
#             with self.subTest(url):
#                 response = await self.client.delete(url)
#                 self.assertEqual(
#                     self.prepare_response_errors,
#                     response,
#                     f'При неккоректном запросе к {url} на удаление '
#                     f'возвращается массив errors')
#                 self.assertIsInstance(
#                     response,
#                     dict,
#                     'Должен возвращаться объект типа dict')
