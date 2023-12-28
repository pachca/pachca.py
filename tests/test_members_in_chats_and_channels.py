from tests.fixtures.errors import PREPARE_RESPONSE_ERRORS
from tests.fixtures.members_chats_channels import (PREPARE_CORRECT_MEMBERS,
                                                   PREPARE_CORRECT_TAGS,
                                                   PREPARE_INCORRECT_MEMBERS,
                                                   PREPARE_INCORRECT_TAGS,
                                                   URL_ADD_MEMBERS,
                                                   URL_ADD_TAGS,
                                                   URL_DEL_MEMBERS,
                                                   URL_DEL_TAG)
from tests.test_base_client import TestBaseClient


class TestMembersInChatsAndChannelsTest(TestBaseClient):
    """Тестирует запросы клиента к ресурсам '/chats/{id}/members',
    /chats/{id}/group_tags.
    """

    def setUp(self) -> None:
        self.url_add_members = URL_ADD_MEMBERS
        self.url_del_member = URL_DEL_MEMBERS
        self.url_add_tags = URL_ADD_TAGS
        self.url_del_tag = URL_DEL_TAG
        self.prepare_correct_members_data = PREPARE_CORRECT_MEMBERS
        self.prepare_correct_tags_data = PREPARE_CORRECT_TAGS
        self.prepare_incorrect_tags_data = PREPARE_INCORRECT_TAGS
        self.prepare_incorrect_members_data = PREPARE_INCORRECT_MEMBERS
        self.prepare_response_errors = PREPARE_RESPONSE_ERRORS
        self.prepare_response_correct_data = {}

        self.url_add_data = (
            self.url_add_members,
            self.url_del_tag
        )

        self.url_del = (
            self.url_del_member,
            self.url_del_tag
        )

        self.prepare_add_correct_data = (
            self.prepare_correct_members_data,
            self.prepare_correct_tags_data
        )

        self.prepare_add_incorrect_data = (
            self.prepare_incorrect_members_data,
            self.prepare_incorrect_tags_data
        )

    async def test_add_correct_data(self) -> None:
        """Тестирует метод 'post'.
        Добавление пользователей в состав участников беседы/канала.
        Добавление тегов в состав участников беседы/канала.

        Проверяет корректность возвращаемых данных
        (без тела ответа) при безошибочном выполнении
        клиентом метода 'post'.
        """
        self.mock.return_value = self.prepare_response_correct_data
        for data, url in zip(
                self.prepare_add_correct_data, self.url_add_data):
            with self.subTest(data=data):
                response = await self.client.post(url, data)
                self.assertEqual(
                    self.prepare_response_correct_data,
                    response,
                    'При безошибочном выполнение запроса '
                    'тело ответа отсутвует')

    async def test_add_incorrect_data(self) -> None:
        """Тестирует метод 'post'.
        Добавление пользователей в состав участников беседы/канала.
        Добавление тегов в состав участников беседы/канала.

        Проверяет корректность возвращаемых данных
        (описание оишбки, содержащееся в массиве errors)
        при выполении клиентом метода 'post' с
        некорректными телом запроса.
        """
        self.mock.return_value = self.prepare_response_errors
        for data, url in zip(
                self.prepare_add_incorrect_data, self.url_add_data):
            with self.subTest(data=data):
                response = await self.client.post(url, data)
                self.assertEqual(
                    self.prepare_response_errors,
                    response,
                    f'При некорректном теле POST-запроса '
                    f'к эндпоинту {url} '
                    'должен вернуться массив errors')
                self.assertIsInstance(
                    response,
                    dict,
                    'Должен возвращаться объект типа dict')

    # async def test_del_correct(self) -> None:
    #     """Тестирует метод 'del'.
    #     Исключение пользователя из состава участников беседы/канала.
    #     Исключение тега из состава участников беседы/канала.

    #     Проверяет корректность возвращаемых данных
    #     (без тела ответа) при безошибочном выполнении
    #     клиентом метода 'del'.
    #     """
    #     self.mock.return_value = self.prepare_response_correct_data
    #     for url in self.url_del:
    #         with self.subTest(url):
    #             response = await self.client.delete(url)
    #             self.assertEqual(
    #                 self.prepare_response_correct_data,
    #                 response,
    #                 'При безошибочном выполнение запроса '
    #                 'тело ответа отсутвует')

    # async def test_del_incorrect(self) -> None:
    #     """Тестирует метод 'del'.
    #     Исключение пользователя из состава участников беседы/канала.
    #     Исключение тега из состава участников беседы/канала.

    #     Проверяет корректность возвращаемых данных
    #     (описание оишбки, содержащееся в массиве errors)
    #     при выполении клиентом метода 'del' с
    #     некорректными параметрами пути.
    #     """
    #     self.mock.return_value = self.prepare_response_errors
    #     for url in self.url_del:
    #         with self.subTest(url):
    #             response = await self.client.delete(url)
    #             self.assertEqual(
    #                 self.prepare_response_errors,
    #                 response,
    #                 f'При неккоректном запросе к {url} на удаление '
    #                 f'возвращается массив errors')
    #             self.assertIsInstance(
    #                 response,
    #                 dict,
    #                 'Должен возвращаться объект типа dict')
