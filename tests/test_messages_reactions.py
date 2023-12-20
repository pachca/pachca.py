import os
import unittest
from unittest.mock import patch

from client.session.client import HttpClient
from tests.fixtures.errors import PREPARE_RESPONSE_ERRORS
from tests.fixtures.messages_reactions import (LIST_REACTIONS, REACTION,
                                               REACTION_INCORRECT,
                                               URL_MESSAGE_REACTIONS)


class MessagesReactionsTest(unittest.IsolatedAsyncioTestCase):

    def setUp(self):
        self.url_messages_reactions = URL_MESSAGE_REACTIONS
        self.prepare_response_errors = PREPARE_RESPONSE_ERRORS
        self.prepare_reaction = REACTION
        self.prepare_reaction_incorrect = REACTION_INCORRECT
        self.prepare_response_list_reactions = LIST_REACTIONS
        self.prepare_response_correct_data = {}

    async def asyncSetUp(self):
        self.client = HttpClient(os.getenv('API_TOKEN'))
        self.patch_client = patch(
            'client.session.client.HttpClient._request')
        self.mock = self.patch_client.start()

    async def asyncTearDown(self):
        self.patch_client.stop()

    async def test_created_reaction(self):
        self.mock.return_value = self.prepare_response_correct_data
        response = await self.client.post(
            self.url_messages_reactions,
            self.prepare_reaction)
        self.assertEqual(
            self.prepare_response_correct_data,
            response,
            'При безошибочном выполнение запроса тело ответа отсутвует')

    async def test_created_reaction_incorrect(self):
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

    async def test_del_reaction(self):
        self.mock.return_value = self.prepare_response_correct_data
        response = await self.client.delete(self.url_messages_reactions)
        self.assertEqual(
            self.prepare_response_correct_data,
            response,
            'При безошибочном выполнение запроса тело ответа отсутвует')

    async def test_del_incorrect(self):
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

    async def test_get_list_reactions(self):
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

    async def test_get_list_reactions_incorrect(self):
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
