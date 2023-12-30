from tests.fixtures.common import TEST_ID
from tests.fixtures.thread import RESPONSE_NEW_THREAD
from tests.test_base_client import TestBaseClient


class TestThred(TestBaseClient):
    """Тестирует запросы бота к ресурсу '/messages/{id}/thread'."""

    async def test_create_thread(self) -> None:
        """Тестирует метод 'create_thread'.
        Создание нового треда к сообщению.

        Проверяет корректность возвращаемых данных
        (объект треда, содержащийся в массиве data)
        при безошибочном выполнении ботом метода 'create_thread'.
        """
        self.mock.return_value = RESPONSE_NEW_THREAD
        response = await self.bot.create_thread(TEST_ID)
        self.assertEqual(
            RESPONSE_NEW_THREAD,
            response,
            'При создании треда возвращается '
            'информация о новом созданном треде')
        self.assertIsInstance(
            response,
            dict,
            'Должен возвращаться объект типа dict')
