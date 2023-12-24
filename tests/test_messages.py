from tests.test_base_client import TestBaseClient
from tests.fixtures.errors import PREPARE_RESPONSE_ERRORS
from tests.fixtures.messages import (EDIT_MESSAGE, INFO_MESSAGES,
                                     LIST_MESSAGES, NEW_MESSAGE,
                                     NEW_MESSAGE_INCORRECT,
                                     RESPONSE_NEW_MESSAGE_DATA,
                                     URL_MESSAGE_INFO, URL_MESSAGES)


class TestMessages(TestBaseClient):
    """Тестирует запросы клиента к ресурсу '/messages'."""

    def setUp(self) -> None:
        self.url_messages = URL_MESSAGES
        self.url_message_info = URL_MESSAGE_INFO
        self.prepare_response_errors = PREPARE_RESPONSE_ERRORS
        self.prepare_new_message = NEW_MESSAGE
        self.prepare_new_message_incorrect = NEW_MESSAGE_INCORRECT
        self.prepare_response_new_message_data = RESPONSE_NEW_MESSAGE_DATA
        self.prepare_info_message = INFO_MESSAGES
        self.prepare_info_list_message = LIST_MESSAGES
        self.prepare_edit_message = EDIT_MESSAGE

    async def test_created_new_messages(self) -> None:
        """Тестирует метод 'post'.
        Создание нового сообщения в беседу или канал,
        личного сообщения пользователю или комментария в тред.

        Проверяет корректность возвращаемых данных
        (объект сообщения, содержащийся в массиве data)
        при безошибочном выполнении клиентом метода 'post'.
        """
        self.mock.return_value = self.prepare_response_new_message_data
        response = await self.client.post(
            self.url_messages,
            self.prepare_new_message)
        self.assertEqual(
            self.prepare_response_new_message_data,
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

    async def test_created_new_messages_incorrect(self) -> None:
        """Тестирует метод 'post'.
        Создание нового сообщения в беседу или канал,
        личного сообщения пользователю или комментария в тред.

        Проверяет корректность возвращаемых данных
        (описание ошибки, содержащееся в массиве errors)
        при выполении клиентом метода 'post' с некорректными телом запроса.
        """
        self.mock.return_value = self.prepare_response_errors
        response = await self.client.post(
            self.url_messages,
            self.prepare_new_message_incorrect)
        self.assertEqual(
            self.prepare_response_errors,
            response,
            'При неккоректном запросе возвращается массив errors')
        self.assertIsInstance(
            response,
            dict,
            'Должен возвращаться объект типа dict')

    async def test_get_message_info(self) -> None:
        """Тестирует метод 'get'.
        Получение информации о сообщение по id.

        Проверяет корректность возвращаемых данных
        (объект сообщения, содержащийся в массиве data)
        при безошибочном выполнении клиентом метода 'get'.
        """
        self.mock.return_value = self.prepare_info_message
        response = await self.client.get(self.url_message_info)
        self.assertEqual(
            self.prepare_info_message,
            response,
            'При корректном запросе в теле ответа '
            'возвращается информация о сообщении')
        self.assertIsInstance(
            response,
            dict,
            'Должен возвращаться объект типа dict')

    async def test_get_message_info_incorrect(self) -> None:
        """Тестирует метод 'get'.
        Получение информации о сообщение по id.

        Проверяет корректность возвращаемых данных
        (описание ошибки, содержащееся в массиве errors)
        при выполении клиентом метода 'get' с
        некорректными параметрами пути.
        """
        self.mock.return_value = self.prepare_response_errors
        response = await self.client.get(self.url_message_info)
        self.assertEqual(
            self.prepare_response_errors,
            response,
            'При запросе к несуществующему id сообщения '
            'возвращается массив errors')
        self.assertIsInstance(
            response,
            dict,
            'Должен возвращаться объект типа dict')

    async def test_get_list_messages(self) -> None:
        """Тестирует метод 'get'.
        Получение списка сообщений.

        Проверяет корректность возвращаемых данных
        (список объектов/сообщений, содержащийся в массиве data)
        при безошибочном выполнении клиентом метода 'get'.
        """
        self.mock.return_value = self.prepare_info_list_message
        response = await self.client.get(self.url_messages)
        self.assertEqual(
            self.prepare_info_list_message,
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

    async def test_get_list_messages_incorrect(self) -> None:
        """Тестирует метод 'get'.
        Получение списка сообщений.

        Проверяет корректность возвращаемых данных
        (описание ошибки, содержащееся в массиве errors)
        при выполении клиентом метода 'get' с
        некорректными параметрами пути.
        """
        self.mock.return_value = self.prepare_response_errors
        response = await self.client.get(self.url_messages)
        self.assertEqual(
            self.prepare_response_errors,
            response,
            'При неккоректном запросе возвращается массив errors')
        self.assertIsInstance(
            response,
            dict,
            'Должен возвращаться объект типа dict')

    async def test_edit_messages(self) -> None:
        """Тестирует метод 'put'.
        Редактирование сообщения по указанному идентификатору.

        Проверяет корректность возвращаемых данных
        (объект сообщения, содержащийся в массиве data)
        при безошибочном выполнении клиентом метода 'put'.
        """
        self.mock.return_value = self.prepare_response_new_message_data
        response = await self.client.put(
            self.url_message_info,
            self.prepare_edit_message)
        self.assertEqual(
            self.prepare_response_new_message_data,
            response,
            'При редактирование сообщения '
            'возвращается информация о сообщении')
        self.assertIsInstance(
            response,
            dict,
            'Должен возвращаться объект типа dict')

    async def test_edit_messages_incorrect(self) -> None:
        """Тестирует метод 'put'.
        Редактирование сообщения по указанному идентификатору.

        Проверяет корректность возвращаемых данных
        (описание ошибки, содержащееся в массиве errors)
        при выполении клиентом метода 'put' с
        некорректным идентификатором сообщения.
        """
        self.mock.return_value = self.prepare_response_errors
        response = await self.client.put(
            self.url_messages,
            self.prepare_new_message_incorrect)
        self.assertEqual(
            self.prepare_response_errors,
            response,
            'При неккоректном запросе возвращается массив errors')
        self.assertIsInstance(
            response,
            dict,
            'Должен возвращаться объект типа dict')
