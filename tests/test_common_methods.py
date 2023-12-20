from tests.fixtures.common import EMPTY_ARRAY_MESSAGE
from tests.fixtures.common_methods import (ERROR_XML,
                                           EXPECT_RESPONSE_DATA_PROPERTIES,
                                           EXPECT_RESPONSE_DATA_UPLOADS,
                                           POST_DATA_UPLOADS, PROPERTIES_URL,
                                           UPLOAD_FILE_INCORRECT_DATA,
                                           UPLOAD_FILE_URL,
                                           UPLOADS_ERROR_MESSAGE, UPLOADS_URL)
from tests.test_base_client import TestBaseClient


class TestCommonMethods(TestBaseClient):
    """Тестирует запросы клиента к '/custom_properties' и '/uploads'."""

    def setUp(self):
        self.base_url_properties = PROPERTIES_URL
        self.base_url_uploads = UPLOADS_URL
        self.base_url_upload_file = UPLOAD_FILE_URL

    async def test_get_custom_properties_correct_data(self) -> None:
        """Тестирует метод 'get'.

        Проверяет корректность возвращаемых данных
        (список объектов дополнительных свойств, содержащийся
        в массиве 'data') при безошибочном выполнении клиентом метода 'get'.
        """
        self.mock_request.return_value = EXPECT_RESPONSE_DATA_PROPERTIES
        response = await self.client.get(self.base_url_properties)
        self.assertEqual(
            response,
            EXPECT_RESPONSE_DATA_PROPERTIES,
            'При корректном запросе в теле ответа '
            'возвращается список объектов дополнительных свойств'
        )

    async def test_post_uploads_correct_data(self) -> None:
        """Тестирует метод 'post'.

        Проверяет корректность возвращаемых данных
        (уникальный набор параметров для загрузки файлов) при
        безошибочном выполнении клиентом метода 'post'.
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
        (отсутствующее тело ответа) при
        безошибочном выполнении клиентом метода 'post'.
        """
        expect_response_data = {}
        self.mock_request.return_value = expect_response_data
        upload_params = POST_DATA_UPLOADS
        upload_file = __file__
        with open(upload_file, "rb") as file:
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
        """Тестирует метод 'post' с некорректными данными.

        Проверяет корректность возвращаемых данных
        (xml, в котором будет расписана ошибка Error, и в поле
        Message будут указаны подробности) при
        выполнении клиентом метода 'post' c некорректными параметрами.
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
