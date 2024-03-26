from pydantic_core import ValidationError
from tests.fixtures.common import TEST_ID, EMPTY_ARRAY
from tests.fixtures.messages_reactions import (LIST_REACTIONS, REACTION,
                                               REACTION_INCORRECT)
from tests.test_base_client import TestBaseClient


class TestMessagesReactions(TestBaseClient):
    """Тестирует запросы клиента к ресурсу '/messages/{id}/reactions'."""

    async def test_add_reaction(self) -> None:
        """Тестирует метод 'add_reaction'.
        Добавление реакции на сообщение.

        Проверяет корректность возвращаемых данных
        (объект задачи, содержащийся в массиве data)
        при безошибочном выполнении ботом метода 'add_reaction'.
        """
        self.mock.return_value = EMPTY_ARRAY
        response = await self.bot.add_reaction(message_id=TEST_ID, code=REACTION)
        self.assertEqual(
            EMPTY_ARRAY,
            response,
            'При безошибочном выполнение запроса тело ответа отсутвует',
        )

    async def test_add_reaction_incorrect(self) -> None:
        """Тестирует метод 'add_reaction'.
        Добавление реакции на сообщение.

        Проверяет корректность возвращаемых данных
        (возникновение ошибки ValidationError)
        при выполнении ботом метода 'add_reaction' с некорректными
        данными.
        """
        with self.assertRaises(
            ValidationError,
            msg=(
                "При выполнении метода 'add_reaction' c некорректным "
                "телом запроса должна возникать ошибка ValidationError"
            ),
        ):
            await self.bot.add_reaction(
                message_id=TEST_ID,
                code=REACTION_INCORRECT,
            )

    async def test_delete_reaction(self) -> None:
        """Тестирует метод 'delete_reaction'.
        Удаление реакции на сообщение.

        Проверяет корректность возвращаемых данных
        (без тела ответа) при безошибочном выполнении
        ботом метода 'delete_reaction'.
        """
        self.mock.return_value = EMPTY_ARRAY
        response = await self.bot.delete_reaction(
            TEST_ID,
            REACTION,
        )
        self.assertEqual(
            EMPTY_ARRAY,
            response,
            'При безошибочном выполнение запроса тело ответа отсутвует',
        )

    async def test_delete_reaction_incorrect(self) -> None:
        """Тестирует метод 'delete_reaction'.
        Удаление реакции на сообщение.

        Проверяет корректность возвращаемых данных
        (возникновение ошибки ValidationError)
        при выполнении клиентом метода 'delete_reaction' с некорректными
        данными.
        """
        with self.assertRaises(
            ValidationError,
            msg=(
                "При выполнении метода 'delete_reaction' c некорректным "
                "телом запроса должна возникать ошибка ValidationError"
            ),
        ):
            await self.bot.delete_reaction(
                message_id=TEST_ID,
                code=REACTION_INCORRECT,
            )

    async def test_get_reactions(self) -> None:
        """Тестирует метод 'get_reactions'.
        Получение актуального списка реакций.

        Проверяет корректность возвращаемых данных
        (список объектов/реакций, содержащийся в массиве data)
        при безошибочном выполнении ботом метода 'get_reactions'.
        """
        self.mock.return_value = LIST_REACTIONS
        response = await self.bot.get_reactions(message_id=TEST_ID)
        self.assertEqual(
            LIST_REACTIONS,
            response,
            'При корректном запросе возвращается список реакций',
        )
        self.assertIsInstance(
            response,
            dict,
            'Должен возвращаться объект типа dict',
        )
        self.assertIsInstance(
            response['data'],
            list,
            'Ключ "data" содержит список',
        )
