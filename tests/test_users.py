from urllib.parse import urljoin

from tests.fixtures.common import (DATA_ARRAY_MESSAGE, EMPTY_ARRAY_MESSAGE,
                                   ERROR_ARRAY_MESSAGE, EXPECT_RESPONSE_ERRORS,
                                   TEST_ID)
from tests.fixtures.users import (EXPECT_RESPONSE_DATA_USER,
                                  EXPECT_RESPONSE_DATA_USERS,
                                  INCORRECT_USER_DATA, NEW_USER_DATA,
                                  UPDATE_USER_DATA, USERS_URL)
from tests.test_base_client import TestBaseClient


class TestUsers(TestBaseClient):
    """Тестирует запросы клиента к ресурсу 'users/'."""

    def setUp(self):
        self.users_url = USERS_URL

    async def test_get_users_correct_data_object_and_list(self) -> None:
        """Тестирует метод 'get'.

        Проверяет корректность возвращаемых данных
        (объект пользователя и список объектов пользователей,
        содержащиеся в массивах данных 'data')
        при безошибочном выполнении клиентом метода 'get'.
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
                self.mock.return_value = data
                response = await self.client.get(url)
                self.assertEqual(
                    response,
                    expect_response_data,
                    DATA_ARRAY_MESSAGE
                )

    async def test_create_user_correct_data(self) -> None:
        """Тестирует метод 'post' с корректным телом запроса.

        Проверяет корректность возвращаемых данных
        (объект пользователя, содержащийся в массиве data)
        при безошибочном выполнении клиентом метода 'post'.
        """
        new_user_data = NEW_USER_DATA
        self.mock.return_value = EXPECT_RESPONSE_DATA_USER
        response = await self.client.post(self.users_url, new_user_data)
        self.assertEqual(
            response,
            EXPECT_RESPONSE_DATA_USER,
            'При создании нового пользователя '
            'возвращается информация о созданном пользователе'
        )

    async def test_create_user_incorrect_data(self) -> None:
        """Тестирует метод 'post' с некорректным телом запроса.

        Проверяет корректность возвращаемых данных
        (опсание ошибки, содержащееся в массиве errors)
        при выполнении клиентом метода 'post' с
        некорректным телом запроса.
        """
        new_user_data = INCORRECT_USER_DATA
        self.mock.return_value = EXPECT_RESPONSE_ERRORS
        response = await self.client.post(self.users_url, new_user_data)
        self.assertEqual(
            response,
            EXPECT_RESPONSE_ERRORS,
            ERROR_ARRAY_MESSAGE
        )

    async def test_update_user_correct_data(self) -> None:
        """Тестирует метод 'put' с корректным телом запроса.

        Проверяет корректность возвращаемых данных
        (объект пользователя, содержащийся в массиве data)
        при безошибочном выполнении клиентом метода 'patch'.
        """
        update_user_data = UPDATE_USER_DATA
        self.mock.return_value = EXPECT_RESPONSE_DATA_USER
        response = await self.client.put(urljoin(
            self.users_url, TEST_ID), update_user_data
        )
        self.assertEqual(
            response,
            EXPECT_RESPONSE_DATA_USER,
            'При редактирование пользователя '
            'возвращается информация о пользователе'
        )

    async def test_update_user_incorrect_data(self) -> None:
        """Тестирует метод 'put' с некорректным телом запроса.

        Проверяет корректность возвращаемых данных
        (опсание ошибки, содержащееся в массиве errors)
        при выполнении клиентом метода 'put' с
        некорректным телом запроса.
        """
        new_user_data = INCORRECT_USER_DATA
        self.mock.return_value = EXPECT_RESPONSE_ERRORS
        response = await self.client.put(
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
        (без тела ответа) при безошибочном выполнении
        клиентом метода 'delete'.
        """
        expect_resposne_data = {}
        self.mock.return_value = {}
        response = await self.client.delete(urljoin(self.users_url, TEST_ID))
        self.assertEqual(
            response,
            expect_resposne_data,
            EMPTY_ARRAY_MESSAGE
        )
