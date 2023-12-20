from urllib.parse import urljoin

from tests.fixtures.common import DATA_ARRAY_MESSAGE, TEST_ID
from tests.fixtures.group_tags import EXPECT_RESPONSE_DATA_GROUP_TAGS, TAGS_URL
from tests.fixtures.users import EXPECT_RESPONSE_DATA_USERS
from tests.test_base_client import TestBaseClient


class TestGroupTags(TestBaseClient):
    """Тестирует запросы клиента к ресурсу 'group_tags/'."""

    def setUp(self):
        self.tags_url = TAGS_URL

    async def test_get_chats_correct_object_and_list_data(self) -> None:
        """Тестирует метод 'get'.

        Проверяет корректность возвращаемых данных
        (список объектов беседы в первом подтесте и список объектов
        пользоваетелй тега - во втором, содержащиеся в массивах 'data')
        при безошибочном выполнении клиентом метода 'get'.
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
