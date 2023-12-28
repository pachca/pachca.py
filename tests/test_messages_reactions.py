from tests.fixtures.errors import PREPARE_RESPONSE_ERRORS
from tests.fixtures.messages_reactions import (LIST_REACTIONS, REACTION,
                                               REACTION_INCORRECT,
                                               URL_MESSAGE_REACTIONS)
from tests.test_base_client import TestBaseClient


class TestMessagesReactions(TestBaseClient):
    """Тестирует запросы клиента к ресурсу '/messages/{id}/reactions'."""

    def setUp(self) -> None:
        self.url_messages_reactions = URL_MESSAGE_REACTIONS
        self.prepare_response_errors = PREPARE_RESPONSE_ERRORS
        self.prepare_reaction = REACTION
        self.prepare_reaction_incorrect = REACTION_INCORRECT
        self.prepare_response_list_reactions = LIST_REACTIONS
        self.prepare_response_correct_data = {}

    async def test_created_reaction(self) -> None:
        """Тестирует метод 'post'.
        Добавление реакции на сообщение.

        Проверяет корректность возвращаемых данных
        (объект задачи, содержащийся в массиве data)
        при безошибочном выполнении клиентом метода 'post'.
        """
        self.mock.return_value = self.prepare_response_correct_data
        response = await self.client.post(
            self.url_messages_reactions,
            self.prepare_reaction)
        self.assertEqual(
            self.prepare_response_correct_data,
            response,
            'При безошибочном выполнение запроса тело ответа отсутвует')

    async def test_created_reaction_incorrect(self) -> None:
        """Тестирует метод 'post'.
        Добавление реакции на сообщение.

        Проверяет корректность возвращаемых данных
        (описание ошибки, содержащееся в массиве errors)
        при выполнении клиентом метода 'post' с некорректными
        данными.
        """
        self.mock.return_value = self.prepare_response_errors
        response = await self.client.post(
            self.url_messages_reactions,
            self.prepare_reaction_incorrect)
        self.assertEqual(
            self.prepare_response_errors,
            response,
            f'При некорректном теле POST-запроса '
            f'к эндпоинту {self.url_messages_reactions} '
            'должен вернуться массив errors')
        self.assertIsInstance(
            response,
            dict,
            'Должен возвращаться объект типа dict')

    async def test_del_reaction(self) -> None:
        """Тестирует метод 'del'.
        Удаление реакции на сообщение.

        Проверяет корректность возвращаемых данных
        (без тела ответа) при безошибочном выполнении
        клиентом метода 'del'.
        """
        self.mock.return_value = self.prepare_response_correct_data
        response = await self.client.delete(self.url_messages_reactions)
        self.assertEqual(
            self.prepare_response_correct_data,
            response,
            'При безошибочном выполнение запроса тело ответа отсутвует')

    async def test_del_incorrect(self) -> None:
        """Тестирует метод 'del'.
        Удаление реакции на сообщение.

        Проверяет корректность возвращаемых данных
        (описание ошибки, содержащееся в массиве errors)
        при выполнении клиентом метода 'del' с некорректными
        данными.
        """
        self.mock.return_value = self.prepare_response_errors
        response = await self.client.delete(
            self.url_messages_reactions,
            data=self.prepare_reaction)
        self.assertEqual(
            self.prepare_response_errors,
            response,
            f'При неккоректном запросе на удаление '
            f'возвращается массив errors')
        self.assertIsInstance(
            response,
            dict,
            'Должен возвращаться объект типа dict')

    async def test_get_list_reactions(self) -> None:
        """Тестирует метод 'get'.
        Получение актуального списка реакций.

        Проверяет корректность возвращаемых данных
        (список объектов/реакций, содержащийся в массиве data)
        при безошибочном выполнении клиентом метода 'get'.
        """
        self.mock.return_value = self.prepare_response_list_reactions
        response = await self.client.get(self.url_messages_reactions)
        self.assertEqual(
            self.prepare_response_list_reactions,
            response,
            'При корректном запросе возвращается список реакций')
        self.assertIsInstance(
            response,
            dict,
            'Должен возвращаться объект типа dict')
        self.assertIsInstance(
            response['data'],
            list,
            'Ключ "data" содержит список')

    async def test_get_list_reactions_incorrect(self) -> None:
        """Тестирует метод 'get'.
        Получение актуального списка реакций.

        Проверяет корректность возвращаемых данных
        (описание ошибки, содержащееся в массиве errors)
        при выполении клиентом метода 'get' с некорректными параметрами пути.
        """
        self.mock.return_value = self.prepare_response_errors
        response = await self.client.get(self.url_messages_reactions)
        self.assertEqual(
            self.prepare_response_errors,
            response,
            f'При неккоректном запросе на удаление '
            f'возвращается массив errors')
        self.assertIsInstance(
            response,
            dict,
            'Должен возвращаться объект типа dict')
