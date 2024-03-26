from pydantic_core import ValidationError
from tests.fixtures.tasks import RESPONSE_CREATED_TASK, TASK, TASK_INCORRECT_1, TASK_INCORRECT_2
from tests.test_base_client import TestBaseClient


class TestTasks(TestBaseClient):
    """Тестирует запросы бота к ресурсу '/tasks'."""

    async def test_create_task(self) -> None:
        """Тестирует метод 'create_task'.
        Создание новой задачи.

        Проверяет корректность возвращаемых данных
        (объект задачи, содержащийся в массиве data)
        при безошибочном выполнении ботом метода 'create_task'.
        """
        self.mock.return_value = RESPONSE_CREATED_TASK
        response = await self.bot.create_task(**TASK)
        self.assertEqual(
            RESPONSE_CREATED_TASK,
            response,
            'При создании задачи возвращается информация о новой задаче',
        )
        self.assertIsInstance(
            response,
            dict,
            'Должен возвращаться объект типа dict',
        )

    async def test_created_task_incorrect(self) -> None:
        """Тестирует метод 'create_task'.
        Создание новой задачи.

        Проверяет корректность возвращаемых данных
        (возникновение ошибки ValidationError)
        при выполении ботом метода 'create_task' с
        некорректными телом запроса.
        """
        with self.assertRaises(
            ValidationError,
            msg=(
                "При выполнении метода 'create_task' c некорректным "
                "телом запроса должна возникать ошибка ValidationError"
            ),
        ):
            await self.bot.create_task(**TASK_INCORRECT_1)
        with self.assertRaises(
            TypeError,
            msg=(
                "При выполнении метода 'create_task' без указания "
                "'kind' должна возникать ошибка TypeError"
            ),
        ):
            await self.bot.create_task(**TASK_INCORRECT_2)
