from pydantic_core import ValidationError
from tests.fixtures.common import TEST_ID
from tests.fixtures.messages import (EDIT_MESSAGE, INFO_MESSAGES,
                                     LIST_MESSAGES, NEW_MESSAGE,
                                     NEW_MESSAGE_INCORRECT,
                                     RESPONSE_NEW_MESSAGE_DATA)
from tests.test_base_client import TestBaseClient


class TestMessages(TestBaseClient):
    """Тестирует запросы бота к ресурсу '/messages'."""

    async def test_send_message(self) -> None:
        """Тестирует метод 'send_message'.
        Создание нового сообщения в беседу или канал,
        личного сообщения пользователю или комментария в тред.

        Проверяет корректность возвращаемых данных
        (объект сообщения, содержащийся в массиве data)
        при безошибочном выполнении ботом метода 'send_message'.
        """
        self.mock.return_value = RESPONSE_NEW_MESSAGE_DATA
        response = await self.bot.send_message(**NEW_MESSAGE)
        self.assertEqual(
            RESPONSE_NEW_MESSAGE_DATA,
            response,
            'При создании нового сообщения '
            'возвращается информация о созданном сообщении')
        self.assertIn(
            'data',
            response,
            'В возвращаемом словаре должен быть ключ "data"')
        self.assertIsInstance(
            response,
            dict,
            'Должен возвращаться объект типа dict')

    async def test_send_message_incorrect(self) -> None:
        """Тестирует метод 'send_message'.
        Создание нового сообщения в беседу или канал,
        личного сообщения пользователю или комментария в тред.

        Проверяет корректность возвращаемых данных
        (возникновение ошибки ValidationError)
        при выполении клиентом метода 'post' с некорректными телом запроса.
        """
        with self.assertRaises(
            ValidationError,
            msg=(
                "При выполнении метода 'send_message' c некорректным "
                "телом запроса должна возникать ошибка ValidationError"
            )
        ):
            mess = await self.bot.send_message(**NEW_MESSAGE_INCORRECT)
            print(mess)

    async def test_get_message_by_id(self) -> None:
        """Тестирует метод 'get_message_by_id'.
        Получение информации о сообщение по id.

        Проверяет корректность возвращаемых данных
        (объект сообщения, содержащийся в массиве data)
        при безошибочном выполнении ботом метода 'get_message_by_id'.
        """
        self.mock.return_value = INFO_MESSAGES
        response = await self.bot.get_message_by_id(id=TEST_ID)
        self.assertEqual(
            INFO_MESSAGES,
            response,
            'При корректном запросе в теле ответа '
            'возвращается информация о сообщении')
        self.assertIsInstance(
            response,
            dict,
            'Должен возвращаться объект типа dict')

    async def test_get_messages(self) -> None:
        """Тестирует метод 'get_messages'.
        Получение списка сообщений  бесед, каналов, тредов и личных сообщений.

        Проверяет корректность возвращаемых данных
        (список объектов/сообщений, содержащийся в массиве data)
        при безошибочном выполнении ботом метода 'get_messages'.
        """
        self.mock.return_value = LIST_MESSAGES
        response = await self.bot.get_messages(chat_id=TEST_ID)
        self.assertEqual(
            LIST_MESSAGES,
            response,
            'При корректном запросе возвращается список сообщений чата')
        self.assertIsInstance(
            response,
            dict,
            'Должен возвращаться объект типа dict')
        self.assertIsInstance(
            response['data'],
            list,
            'Ключ "data" содержит список')

    async def test_edit_message(self) -> None:
        """Тестирует метод 'edit_message'.
        Редактирование сообщения по указанному идентификатору.

        Проверяет корректность возвращаемых данных
        (объект сообщения, содержащийся в массиве data)
        при безошибочном выполнении ботом метода 'edit_message'.
        """
        self.mock.return_value = RESPONSE_NEW_MESSAGE_DATA
        response = await self.bot.edit_message(TEST_ID, EDIT_MESSAGE)
        self.assertEqual(
            RESPONSE_NEW_MESSAGE_DATA,
            response,
            'При редактирование сообщения '
            'возвращается информация о сообщении')
        self.assertIsInstance(
            response,
            dict,
            'Должен возвращаться объект типа dict')

    async def test_edit_message_incorrect(self) -> None:
        """Тестирует метод 'edit_message'.
        Редактирование сообщения по указанному идентификатору.

        Проверяет корректность возвращаемых данных
        (овозникновение ошибки ValidationError)
        при выполении ботом метода 'edit_message' с
        некорректным телом запроса.
        """
        with self.assertRaises(
            ValidationError,
            msg=(
                "При выполнении метода 'edit_message' c некорректным "
                "телом запроса должна возникать ошибка ValidationError"
            )
        ):
            await self.bot.edit_message(TEST_ID, NEW_MESSAGE_INCORRECT)
