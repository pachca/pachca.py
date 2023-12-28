from tests.fixtures.errors import PREPARE_RESPONSE_ERRORS
from tests.fixtures.tasks import (RESPONSE_CREATED_TASK, TASK, TASK_INCORRECT,
                                  URL_TASKS)
from tests.test_base_client import TestBaseClient


class TestTasks(TestBaseClient):
    """Тестирует запросы клиента к ресурсу '/tasks'."""

    def setUp(self) -> None:
        self.url_tasks = URL_TASKS
        self.prepare_response_errors = PREPARE_RESPONSE_ERRORS
        self.prepare_task = TASK
        self.prepare_task_incorrect = TASK_INCORRECT
        self.prepare_response_created_task = RESPONSE_CREATED_TASK
        self.prepare_response_correct_data = {}

    async def test_created_new_task(self) -> None:
        """Тестирует метод 'post'.
        Создание новой задачи.

        Проверяет корректность возвращаемых данных
        (объект задачи, содержащийся в массиве data)
        при безошибочном выполнении клиентом метода 'post'.
        """
        self.mock.return_value = self.prepare_response_created_task
        response = await self.client.post(
            self.url_tasks, self.prepare_task)
        self.assertEqual(
            self.prepare_response_created_task,
            response,
            'При создании задачи возвращается информация о новой задаче')
        self.assertIsInstance(
            response,
            dict,
            'Должен возвращаться объект типа dict')

    async def test_created_new_task_incorrect(self) -> None:
        """Тестирует метод 'post'.
        Создание новой задачи.

        Проверяет корректность возвращаемых данных
        (описание ошибки, содержащееся в массиве errors)
        при выполнении клиентом метода 'post' с некорректными
        данными.
        """
        self.mock.return_value = self.prepare_response_errors
        response = await self.client.post(
            self.url_tasks, self.prepare_task_incorrect)
        self.assertEqual(
            self.prepare_response_errors,
            response,
            'При неккоректном запросе возвращается массив errors')
        self.assertIsInstance(
            response,
            dict,
            'Должен возвращаться объект типа dict')
