import os
import unittest
from unittest.mock import patch

from client.session.client import HttpClient
from tests.fixtures.errors import PREPARE_RESPONSE_ERRORS
from tests.fixtures.messages import (EDIT_MESSAGE, INFO_MESSAGES,
                                     LIST_MESSAGES, NEW_MESSAGE,
                                     NEW_MESSAGE_INCORRECT,
                                     RESPONSE_NEW_MESSAGE_DATA,
                                     URL_MESSAGE_INFO, URL_MESSAGES)


class MessagesTest(unittest.IsolatedAsyncioTestCase):

    def setUp(self):
        self.url_messages = URL_MESSAGES
        self.url_message_info = URL_MESSAGE_INFO
        self.prepare_response_errors = PREPARE_RESPONSE_ERRORS
        self.prepare_new_message = NEW_MESSAGE
        self.prepare_new_message_incorrect = NEW_MESSAGE_INCORRECT
        self.prepare_response_new_message_data = RESPONSE_NEW_MESSAGE_DATA
        self.prepare_info_message = INFO_MESSAGES
        self.prepare_info_list_message = LIST_MESSAGES
        self.prepare_edit_message = EDIT_MESSAGE

    async def asyncSetUp(self):
        self.client = HttpClient(os.getenv('API_TOKEN'))
        self.patch_client = patch(
            'client.session.client.HttpClient._request')
        self.mock = self.patch_client.start()

    async def asyncTearDown(self):
        self.patch_client.stop()

    async def test_created_new_messages(self):
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

    async def test_created_new_messages_incorrect(self):
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

    async def test_get_message_info(self):
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

    async def test_get_message_info_incorrect(self):
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

    async def test_get_list_messages(self):
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

    async def test_get_list_messages_incorrect(self):
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

    async def test_edit_messages(self):
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

    async def test_edit_messages_incorrect(self):
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
