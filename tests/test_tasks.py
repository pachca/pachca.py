import os
import unittest
from unittest.mock import patch

from client.session.client import HttpClient
from tests.fixtures.errors import PREPARE_RESPONSE_ERRORS
from tests.fixtures.tasks import (RESPONSE_CREATED_TASK, TASK, TASK_INCORRECT,
                                  URL_TASKS)


class TasksTest(unittest.IsolatedAsyncioTestCase):

    def setUp(self):
        self.url_tasks = URL_TASKS
        self.prepare_response_errors = PREPARE_RESPONSE_ERRORS
        self.prepare_task = TASK
        self.prepare_task_incorrect = TASK_INCORRECT
        self.prepare_response_created_task = RESPONSE_CREATED_TASK
        self.prepare_response_correct_data = {}

    async def asyncSetUp(self):
        self.client = HttpClient(os.getenv('API_TOKEN'))
        self.patch_client = patch(
            'client.session.client.HttpClient._request')
        self.mock = self.patch_client.start()

    async def asyncTearDown(self):
        self.patch_client.stop()

    async def test_created_new_task(self):
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

    async def test_created_new_task_incorrect(self):
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
