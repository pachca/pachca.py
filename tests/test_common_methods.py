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
        (итоговый файл, который  будет использоваться для
        прикрепления к сообщению и в других методах) при
        безошибочном выполнении ботом метода 'upload_file'.
        """
        upload_file_path = os.path.abspath(__file__).replace('\\', '/')
        self.mock.return_value = EXPECT_RESPONSE_DATA_UPLOADS
        response = await self.bot.upload_file(upload_file_path, file_type=EXPECT_RESPONSE_DATA_UPLOAD_FILE['file_type'])

        self.assertEqual(
            response.key,
            EXPECT_RESPONSE_DATA_UPLOAD_FILE['key'],
            msg="Проверка ключа файла"
        )
        self.assertEqual(
            response.name,
            EXPECT_RESPONSE_DATA_UPLOAD_FILE['name'],
            msg="Проверка имени файла"
        )
        self.assertEqual(
            response.file_type,
            EXPECT_RESPONSE_DATA_UPLOAD_FILE['file_type'],
            msg="Проверка типа файла"
        )
        self.assertEqual(
            response.size,
            os.path.getsize(upload_file_path),
            msg="Проверка размера файла"
        )
