from tests.fixtures.common import TEST_ID
from tests.fixtures.group_tags import EXPECT_RESPONSE_DATA_GROUP_TAGS
from tests.fixtures.users import EXPECT_RESPONSE_DATA_USERS
from tests.test_base_client import TestBaseClient


class TestGroupTags(TestBaseClient):
    """Тестирует запросы бота к ресурсу 'group_tags/'."""

    async def test_get_group_tags_correct_data(self) -> None:
        """Тестирует метод 'get_chats'.

        Проверяет корректность возвращаемых данных
        (список объектов тегов, содержащиеся в массиве 'data')
        при безошибочном выполении ботом метода 'get_group_tags'.
        """
        self.mock.return_value = EXPECT_RESPONSE_DATA_GROUP_TAGS
        response = await self.bot.get_group_tags()
        self.assertEqual(
            response,
            EXPECT_RESPONSE_DATA_GROUP_TAGS,
            "При безошибочном выполении ботом метода 'get_group_tags' "
            "возвращается список объектов тегов."
        )

    async def test_get_tag_users_correct_data(self) -> None:
        """Тестирует метод 'get_tag_users'.

        Проверяет корректность возвращаемых данных
        (список объектов пользователей тега, содержащийся в массиве 'data')
        при безошибочном выполении ботом метода 'get_tag_users'.
        """
        self.mock.return_value = EXPECT_RESPONSE_DATA_USERS
        response = await self.bot.get_tag_users(TEST_ID)
        self.assertEqual(
            response,
            EXPECT_RESPONSE_DATA_USERS,
            "При безошибочном выполении ботом метода 'get_tag_users' "
            "возвращается список объектов пользователей тега. "
        )
