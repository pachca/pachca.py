from tests.fixtures.errors import PREPARE_RESPONSE_ERRORS
from tests.fixtures.thread import (RESPONSE_CREATED_EARLIER_THREAD,
                                   RESPONSE_NEW_THREAD, URL_EARLIER_THREAD,
                                   URL_NEW_THREAD)
from tests.test_base_client import TestBaseClient


class TestThred(TestBaseClient):
    """Тестирует запросы клиента к ресурсу '/messages/{id}/thread'."""

    def setUp(self) -> None:
        self.request_body = None
        self.url_create_new_thread = URL_NEW_THREAD
        self.url_created_earlier_thread = URL_EARLIER_THREAD
        self.prepare_response_errors = PREPARE_RESPONSE_ERRORS
        self.prepare_response_new_thred = RESPONSE_NEW_THREAD
        self.prepare_response_earlier_thred = RESPONSE_CREATED_EARLIER_THREAD

    async def test_created_new_tread(self) -> None:
        """Тестирует метод 'post'.
        Создание нового треда к сообщению.

        Проверяет корректность возвращаемых данных
        (объект треда, содержащийся в массиве data)
        при безошибочном выполнении клиентом метода 'post'.
        """
        self.mock.return_value = self.prepare_response_new_thred
        response = await self.client.post(
            self.url_create_new_thread, self.request_body)
        self.assertEqual(
            self.prepare_response_new_thred,
            response,
            'При создании треда возвращается '
            'информация о новом созданном треде')
        self.assertIsInstance(
            response,
            dict,
            'Должен возвращаться объект типа dict')

    async def test_created_earlier_tread(self) -> None:
        """Тестирует метод 'post'.
        Создание нового треда к сообщению.

        Проверяет корректность возвращаемых данных
        (объект ранее созданного треда, содержащийся в массиве data)
        при выполнении клиентом метода 'post' с идентификатором сообщения,
        к которому ранее был создан тред.
        """
        self.mock.return_value = self.prepare_response_earlier_thred
        response = await self.client.post(
            self.url_created_earlier_thread, self.request_body)
        self.assertEqual(
            self.prepare_response_earlier_thred,
            response,
            'Если у сообщения уже было создан тред, '
            'то в ответе на запрос вернётся информация '
            'об уже созданном раннее треде.')
        self.assertIsInstance(
            response,
            dict,
            'Должен возвращаться объект типа dict')

    async def test_created_new_tread_incorrect(self) -> None:
        """Тестирует метод 'post'.
        Создание нового треда к сообщению.

        Проверяет корректность возвращаемых данных
        (описание ошибки, содержащееся в массиве errors)
        при выполнении клиентом метода 'post' с некорректным
        идентификатором сообщения.
        """
        self.mock.return_value = self.prepare_response_errors
        response = await self.client.post(
            self.url_create_new_thread, self.request_body)
        self.assertEqual(
            self.prepare_response_errors,
            response,
            'При неккоректном запросе возвращается массив errors')
        self.assertIsInstance(
            response,
            dict,
            'Должен возвращаться объект типа dict')
