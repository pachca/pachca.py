import os
import unittest
from unittest.mock import patch
from urllib.parse import urljoin

from client.session.client import HttpClient

from .fixtures.chats import (CHATS_URL, EXPECT_RESPONSE_DATA_CHAT,
                             EXPECT_RESPONSE_DATA_CHATS, INCORRECT_CHAT_DATA,
                             NEW_CHAT_DATA, UPDATE_CHAT_DATA)
from .fixtures.common import (DATA_ARRAY_MESSAGE, EMPTY_ARRAY_MESSAGE,
                              ERROR_ARRAY_MESSAGE, EXPECT_RESPONSE_ERRORS,
                              PATCH_OBJECT, TEST_ID)
from .fixtures.common_methods import (ERROR_XML,
                                      EXPECT_RESPONSE_DATA_PROPERTIES,
                                      EXPECT_RESPONSE_DATA_UPLOADS,
                                      POST_DATA_UPLOADS, PROPERTIES_URL,
                                      UPLOAD_FILE_INCORRECT_DATA,
                                      UPLOAD_FILE_URL, UPLOADS_ERROR_MESSAGE,
                                      UPLOADS_URL)
from .fixtures.group_tags import EXPECT_RESPONSE_DATA_GROUP_TAGS, TAGS_URL
from .fixtures.users import (EXPECT_RESPONSE_DATA_USER,
                             EXPECT_RESPONSE_DATA_USERS, INCORRECT_USER_DATA,
                             NEW_USER_DATA, UPDATE_USER_DATA, USERS_URL)


class BaseTest(unittest.IsolatedAsyncioTestCase):
    """Базовый класс тестирования."""

    async def asyncSetUp(self):
        self.client = HttpClient(os.getenv("API_TOKEN"))
        self.mock_get_patcher = patch(PATCH_OBJECT)
        self.mock_request = self.mock_get_patcher.start()

    async def asyncTearDown(self):
        self.mock_get_patcher.stop()


class TestUsers(BaseTest):
    """Тестирует запросы клиента к ресурсу 'users/'."""

    def setUp(self) -> None:
        self.users_url = USERS_URL

    async def test_get_users_correct_data_object_and_list(self) -> None:
        """Тестирует метод 'get'

        Поверяет корректность возвращаемых данных
        (объект пользователя и список объектов пользователей,
        содержащиеся в массивах данных 'data')
        при безошибочном выполении клиентом метода 'get'.
        """
        response_data = (
            EXPECT_RESPONSE_DATA_USERS,
            EXPECT_RESPONSE_DATA_USER
        )
        urls = (
            self.users_url,
            urljoin(self.users_url, TEST_ID)
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

    async def test_create_user_correct_data(self) -> None:
        """Тестирует метод 'post'.

        Проверяет корректность возвращаемых данных
        (объект пользователя, содержащийся в массиве data)
        при безошибочном выполении клиентом метода 'post'.
        """
        new_user_data = NEW_USER_DATA
        self.mock_request.return_value = EXPECT_RESPONSE_DATA_USER
        response = await self.client.post(self.users_url, new_user_data)
        self.assertEqual(
            response,
            EXPECT_RESPONSE_DATA_USER,
            DATA_ARRAY_MESSAGE
        )

    async def test_create_user_incorrect_data(self) -> None:
        """Тестирует метод 'post'

        Проверяет корректность возвращаемых данных
        (опсание оишбки, содержащееся в массиве errors)
        при выполении клиентом метода 'post' с
        некорректными телом запроса.
        """
        new_user_data = INCORRECT_USER_DATA
        self.mock_request.return_value = EXPECT_RESPONSE_ERRORS
        response = await self.client.post(self.users_url, new_user_data)
        self.assertEqual(
            response,
            EXPECT_RESPONSE_ERRORS,
            ERROR_ARRAY_MESSAGE
        )

    async def test_update_user_correct_data(self) -> None:
        """Тестирует метод 'patch'

        Проверяет корректность возвращаемых данных
        (объект пользователя, содержащийся в массиве data)
        при безошибочном выполении клиентом метода 'patch'.
        """
        update_user_data = UPDATE_USER_DATA
        self.mock_request.return_value = EXPECT_RESPONSE_DATA_USER
        response = await self.client.patch(urljoin(
            self.users_url, TEST_ID), update_user_data
        )
        self.assertEqual(
            response,
            EXPECT_RESPONSE_DATA_USER,
            DATA_ARRAY_MESSAGE
        )

    async def test_update_user_incorrect_data(self) -> None:
        """Тестирует метод 'patch'.

        Проверяет корректность возвращаемых данных
        (опсание оишбки, содержащееся в массиве errors)
        при выполении клиентом метода 'patch' с
        некорректными телом запроса.
        """
        new_user_data = INCORRECT_USER_DATA
        self.mock_request.return_value = EXPECT_RESPONSE_ERRORS
        response = await self.client.patch(
            urljoin(self.users_url, TEST_ID),
            new_user_data
        )
        self.assertEqual(
            response,
            EXPECT_RESPONSE_ERRORS,
            ERROR_ARRAY_MESSAGE
        )

    async def test_delete_user_correct_data(self) -> None:
        """Тестирует метод 'delete'.

        Проверяет корректность возвращаемых данных
        (без тела ответа) при безошибочном выполении
        клиентом метода 'delete'.
        """
        expect_resposne_data = {}
        self.mock_request.return_value = {}
        response = await self.client.delete(urljoin(self.users_url, TEST_ID))
        self.assertEqual(
            response,
            expect_resposne_data,
            EMPTY_ARRAY_MESSAGE
        )


class TestChats(BaseTest):
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
            DATA_ARRAY_MESSAGE
        )

    async def test_create_chats_incorrect_data(self) -> None:
        """Тестирует метод 'post'c некорректным телом запроса.

        Проверяет корректность возвращаемых данных
        (опсание оишбки, содержащееся в массиве errors)
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
        """Тестирует метод 'patch' c корректным телом запроса.

        Проверяет корректность возвращаемых данных
        (объект беседы, содержащийся в массиве 'data')
        при безошибочном выполении клиентом метода 'patch'.
        """
        update_chat_data = UPDATE_CHAT_DATA
        self.mock_request.return_value = EXPECT_RESPONSE_DATA_CHAT
        response = await self.client.patch(
            urljoin(self.chats_url, TEST_ID),
            update_chat_data
        )
        self.assertEqual(
            response,
            EXPECT_RESPONSE_DATA_CHAT,
            DATA_ARRAY_MESSAGE
        )

    async def test_update_chat_incorrect_data(self) -> None:
        """Тестирует метод 'patch'c некорректным телом запроса.

        Проверяет корректность возвращаемых данных
        (опсание оишбки, содержащееся в массиве errors)
        при выполении клиентом метода 'patch' с
        некорректными телом запроса.
        """
        new_chat_data = INCORRECT_CHAT_DATA
        self.mock_request.return_value = EXPECT_RESPONSE_ERRORS
        response = await self.client.patch(
            urljoin(self.chats_url, TEST_ID),
            new_chat_data
        )
        self.assertEqual(
            response,
            EXPECT_RESPONSE_ERRORS,
            ERROR_ARRAY_MESSAGE
        )


class TestGroupTags(BaseTest):
    """Тестирует запросы клиента к ресурсу 'group_tags/'."""

    def setUp(self):
        self.tags_url = TAGS_URL

    async def test_get_chats_correct_object_and_list_data(self) -> None:
        """Тестирует метод 'get'.

        Проверяет корректность возвращаемых данных
        (список объектов беседы в первом поддесте и список объектов
        пользоваетелй тега - во втором, содержащиеся в массивах 'data')
        при безошибочном выполении клиентом метода 'get'.
        """
        response_data = (
            EXPECT_RESPONSE_DATA_GROUP_TAGS,
            EXPECT_RESPONSE_DATA_USERS
        )
        urls = (
            self.tags_url,
            urljoin(urljoin(self.tags_url, TEST_ID), 'users/')
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


class TestCommonMethods(BaseTest):
    """Тестирует запросы клиента к '/custom_properties' и '/uploads'."""

    def setUp(self):
        self.base_url_properties = PROPERTIES_URL
        self.base_url_uploads = UPLOADS_URL
        self.base_url_upload_file = UPLOAD_FILE_URL

    async def test_get_custom_properties_correct_data(self) -> None:
        """Тестирует метод 'get'.

        Проверяет корректность возвращаемых данных
        (список объектов дополнительных свойств, содержащийся
        в массиве 'data') при безошибочном выполении клиентом метода 'get'.
        """
        self.mock_request.return_value = EXPECT_RESPONSE_DATA_PROPERTIES
        response = await self.client.get(self.base_url_properties)
        self.assertEqual(
            response,
            EXPECT_RESPONSE_DATA_PROPERTIES,
            DATA_ARRAY_MESSAGE
        )

    async def test_post_uploads_correct_data(self) -> None:
        """Тестирует метод 'post'.

        Проверяет корректность возвращаемых данных
        (уникальный набор параметров для загрузки файлов) при
        безошибочном выполении клиентом метода 'post'.
        """
        self.mock_request.return_value = EXPECT_RESPONSE_DATA_UPLOADS
        response = await self.client.post(self.base_url_uploads, None)
        self.assertEqual(
            response,
            EXPECT_RESPONSE_DATA_UPLOADS,
            UPLOADS_ERROR_MESSAGE
        )

    async def test_upload_file_correct_data(self) -> None:
        """Тестирует метод 'post с корректными данными'.

        Проверяет корректность возвращаемых данных
        (отсутствующее тело ответ) при
        безошибочном выполении клиентом метода 'post'.
        """
        expect_response_data = {}
        self.mock_request.return_value = expect_response_data
        upload_params = POST_DATA_UPLOADS
        file_path = os.path.join(
            os.path.dirname(__file__), 'test_http_client.py'
        )
        with open(file_path, "rb") as file:
            response = await self.client.post(
                self.base_url_upload_file,
                {**upload_params, "file": file}
            )
        self.assertEqual(
            response,
            expect_response_data,
            EMPTY_ARRAY_MESSAGE
        )

    async def test_upload_file_incorrect_data(self) -> None:
        """Тестирует метод 'post с некорректными данными'.

        Проверяет корректность возвращаемых данных
        (xml, в котором будет расписана ошибка Error и в поле
        Message будут указаны подробности) при
        выполении клиентом метода 'post' c с некоректынми параметрами.
        """
        self.mock_request.return_value = {"text": ERROR_XML}
        upload_params = UPLOAD_FILE_INCORRECT_DATA
        response = await self.client.post(
            self.base_url_upload_file, upload_params
        )
        self.assertIn("InvalidRequest", response["text"])
        self.assertIn(
            "Некорректный запрос. Проверьте параметры.", response["text"]
        )


if __name__ == "__main__":
    unittest.main()
