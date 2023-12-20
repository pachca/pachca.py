import os
import unittest
from unittest.mock import patch

from client.session.client import HttpClient
from tests.fixtures.errors import PREPARE_RESPONSE_ERRORS
from tests.fixtures.thread import (RESPONSE_CREATED_EARLIER_THREAD,
                                   RESPONSE_NEW_THREAD, URL_EARLIER_THREAD,
                                   URL_NEW_THREAD)


class ThredTest(unittest.IsolatedAsyncioTestCase):

    def setUp(self):
        self.request_body = None
        self.url_create_new_thread = URL_NEW_THREAD
        self.url_created_earlier_thread = URL_EARLIER_THREAD
        self.prepare_response_errors = PREPARE_RESPONSE_ERRORS
        self.prepare_response_new_thred = RESPONSE_NEW_THREAD
        self.prepare_response_earlier_thred = RESPONSE_CREATED_EARLIER_THREAD

    async def asyncSetUp(self):
        self.client = HttpClient(os.getenv('API_TOKEN'))
        self.patch_client = patch(
            'client.session.client.HttpClient._request')
        self.mock = self.patch_client.start()

    async def asyncTearDown(self):
        self.patch_client.stop()

    async def test_created_new_tread(self):
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

    async def test_created_earlier_tread(self):
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

    async def test_created_new_tread_incorrect(self):
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
