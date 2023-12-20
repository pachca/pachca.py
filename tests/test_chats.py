from urllib.parse import urljoin

from tests.fixtures.chats import (CHATS_URL, EXPECT_RESPONSE_DATA_CHAT,
                                  EXPECT_RESPONSE_DATA_CHATS,
                                  INCORRECT_CHAT_DATA, NEW_CHAT_DATA,
                                  UPDATE_CHAT_DATA)
from tests.fixtures.common import (DATA_ARRAY_MESSAGE, ERROR_ARRAY_MESSAGE,
                                   EXPECT_RESPONSE_ERRORS, TEST_ID)
from tests.test_base_client import TestBaseClient


class TestChats(TestBaseClient):
    """Тестирует запросы клиента к ресурсу 'chats/'."""

    def setUp(self):
        self.chats_url = CHATS_URL

    async def test_get_chats_correct_object_and_list_data(self) -> None:
        """Тестирует метод 'get'.

        Проверяет корректность возвращаемых данных
        (объект беседы и список объектов бесед,
        содержащиеся в массивах 'data')
        при безошибочном выполении клиентом метода 'get'.
        """
        response_data = (
            EXPECT_RESPONSE_DATA_CHATS,
            EXPECT_RESPONSE_DATA_CHAT
        )
        urls = (
            self.chats_url,
            urljoin(self.chats_url, TEST_ID)
        )
        for data, url in zip(response_data, urls):
            with self.subTest(data=data, url=url):
                expect_response_data = data
                self.mock_request.return_value = data
                response = await self.client.get(url)
                self.assertEqual(
                    response,
                    expect_response_data,
                    DATA_ARRAY_MESSAGE
                )

    async def test_create_chats_correct_data(self) -> None:
        """Тестирует метод 'post' c корректным телом запроса.

        Проверяет корректность возвращаемых данных
        (объект беседы, содержащийся в массиве 'data')
        при безошибочном выполении клиентом метода 'post'.
        """
        new_chat_data = NEW_CHAT_DATA
        self.mock_request.return_value = EXPECT_RESPONSE_DATA_CHAT
        response = await self.client.post(self.chats_url, new_chat_data)
        self.assertEqual(
            response,
            EXPECT_RESPONSE_DATA_CHAT,
            'При создании новой беседы/канала '
            'возвращается информация о созданном объекте'
        )

    async def test_create_chats_incorrect_data(self) -> None:
        """Тестирует метод 'post'c некорректным телом запроса.

        Проверяет корректность возвращаемых данных
        (опсание ошибки, содержащееся в массиве errors)
        при выполении клиентом метода 'post' с
        некорректными телом запроса.
        """
        new_chat_data = INCORRECT_CHAT_DATA
        self.mock_request.return_value = EXPECT_RESPONSE_ERRORS
        response = await self.client.post(self.chats_url, new_chat_data)
        self.assertEqual(
            response,
            EXPECT_RESPONSE_ERRORS,
            ERROR_ARRAY_MESSAGE
        )

    async def test_update_chats_correct_data(self) -> None:
        """Тестирует метод 'put' c корректным телом запроса.

        Проверяет корректность возвращаемых данных
        (объект беседы, содержащийся в массиве 'data')
        при безошибочном выполении клиентом метода 'put'.
        """
        update_chat_data = UPDATE_CHAT_DATA
        self.mock_request.return_value = EXPECT_RESPONSE_DATA_CHAT
        response = await self.client.put(
            urljoin(self.chats_url, TEST_ID),
            update_chat_data
        )
        self.assertEqual(
            response,
            EXPECT_RESPONSE_DATA_CHAT,
            'При редактирование беседы/канала '
            'возвращается информация об обновленном объекте'
        )

    async def test_update_chat_incorrect_data(self) -> None:
        """Тестирует метод 'put'c некорректным телом запроса.

        Проверяет корректность возвращаемых данных
        (опсание ошибки, содержащееся в массиве errors)
        при выполении клиентом метода 'put' с
        некорректными телом запроса.
        """
        new_chat_data = INCORRECT_CHAT_DATA
        self.mock_request.return_value = EXPECT_RESPONSE_ERRORS
        response = await self.client.put(
            urljoin(self.chats_url, TEST_ID),
            new_chat_data
        )
        self.assertEqual(
            response,
            EXPECT_RESPONSE_ERRORS,
            ERROR_ARRAY_MESSAGE
        )
