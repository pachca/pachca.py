import os

from tests.fixtures.common_methods import (EXPECT_RESPONSE_DATA_UPLOAD_FILE,
                                           EXPECT_RESPONSE_DATA_UPLOADS)
from tests.test_base_client import TestBaseClient


class TestCommonMethods(TestBaseClient):
    """Тестирует запросы клиента к '/custom_properties' и '/uploads'."""

    # async def test_get_custom_properties_correct_data(self) -> None:
    #     """Тестирует метод 'get'.

    #     Проверяет корректность возвращаемых данных
    #     (список объектов дополнительных свойств, содержащийся
    #     в массиве 'data') при безошибочном выполнении клиентом метода 'get'.
    #     """
    #     self.mock.return_value = EXPECT_RESPONSE_DATA_PROPERTIES
    #     response = await self.client.get(self.base_url_properties)
    #     self.assertEqual(
    #         response,
    #         EXPECT_RESPONSE_DATA_PROPERTIES,
    #         'При корректном запросе в теле ответа '
    #         'возвращается список объектов дополнительных свойств'
    #     )

    async def test_upload_file_correct_data(self) -> None:
        """Тестирует метод 'upload_file' с корректными данными'.

        Проверяет корректность возвращаемых данных
        (итоговый путь к файлу, который  будет использоваться для
        его прикрепления к сообщению и в других методах) при
        безошибочном выполнении ботом метода 'upload_file'.
        """
        upload_file_path = os.path.abspath(__file__).replace('\\', '/')
        upload_file_name = upload_file_path.split('/')[-1]
        expect_response_data = (
            EXPECT_RESPONSE_DATA_UPLOAD_FILE + upload_file_name
        )
        self.mock.return_value = EXPECT_RESPONSE_DATA_UPLOADS
        response = await self.bot.upload_file(upload_file_path, file_type='file')
        self.assertEqual(
            response,
            expect_response_data,
            msg=(
                "При безошибочном выполнении ботом метода 'upload_file' "
                "должен возвращаться итоговый путь к файлу, который "
                "будет использоваться для его прикрепления к сообщению "
                "и в других методах."
            )
        )
