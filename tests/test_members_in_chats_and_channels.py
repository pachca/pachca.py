from pydantic_core import ValidationError
from tests.fixtures.common import TEST_ID, EMPTY_ARRAY
from tests.fixtures.members_chats_channels import (PREPARE_CORRECT_MEMBERS,
                                                   PREPARE_CORRECT_TAGS,
                                                   PREPARE_INCORRECT_MEMBERS,
                                                   PREPARE_INCORRECT_TAGS,
                                                   DELETE_INCORRECT_MEMBERS,
                                                   DELETE_INCORRECT_TAGS)
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
            id=TEST_ID, member_ids=PREPARE_CORRECT_MEMBERS
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
                id=TEST_ID, member_ids=PREPARE_INCORRECT_MEMBERS
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
                id=TEST_ID, group_tag_ids=PREPARE_INCORRECT_TAGS
            )

    async def test_delete_member_in_chat_correct(self) -> None:
        """Тестирует метод 'delete_member_in_chat'.
        Исключение пользователя из состава участников беседы/канала.

        Проверяет корректность возвращаемых данных
        (без тела ответа) при безошибочном выполнении
        метода 'delete_member_in_chat'.
        """
        self.mock.return_value = EMPTY_ARRAY
        response = await self.bot.delete_member_in_chat(
            id=TEST_ID,
            member_id=TEST_ID,
        )
        self.assertEqual(
            EMPTY_ARRAY,
            response,
            'При безошибочном выполнение запроса тело ответа отсутвует',
        )

    async def test_delete_member_in_chat_incorrect(self) -> None:
        """Тестирует метод 'delete_member_in_chat'.
        Исключение пользователя из состава участников беседы/канала.

        Проверяет корректность возвращаемых данных
        (описание оишбки, содержащееся в массиве errors)
        при выполении клиентом метода 'delete_member_in_chat' с
        некорректными параметрами пути.
        """
        with self.assertRaises(
            TypeError,
            msg=(
                "При выполнении метода 'delete_member_in_chat' c некорректным "
                "телом запроса должна возникать ошибка TypeError"
            ),
        ):
            await self.bot.delete_member_in_chat(
                **DELETE_INCORRECT_MEMBERS
            )

    async def test_delete_delete_tag_in_chat_correct(self) -> None:
        """Тестирует метод 'delete_tag_in_chat'.
        Исключение тега из состава участников беседы/канала.

        Проверяет корректность возвращаемых данных
        (без тела ответа) при безошибочном выполнении
        метода 'delete_tag_in_chat'.
        """
        self.mock.return_value = EMPTY_ARRAY
        response = await self.bot.delete_tag_in_chat(
            id=TEST_ID,
            group_tag_id=TEST_ID,
        )
        self.assertEqual(
            EMPTY_ARRAY,
            response,
            'При безошибочном выполнение запроса тело ответа отсутвует',
        )

    async def test_delete_delete_tag_in_chat_correct(self) -> None:
        """Тестирует метод 'delete_tag_in_chat'.
        Исключение тега из состава участников беседы/канала.

        Проверяет корректность возвращаемых данных
        (без тела ответа) при безошибочном выполнении
        метода 'delete_tag_in_chat'.
        """
        with self.assertRaises(
            TypeError,
            msg=(
                "При выполнении метода 'delete_tag_in_chat' c некорректным "
                "телом запроса должна возникать ошибка TypeError"
            ),
        ):
            await self.bot.delete_tag_in_chat(
                **DELETE_INCORRECT_TAGS
            )
