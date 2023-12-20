import os
import unittest
from unittest.mock import patch

from client.session.client import HttpClient
from tests.fixtures.common import PATCH_OBJECT


class TestBaseClient(unittest.IsolatedAsyncioTestCase):
    """Базовый класс тестирования."""

    async def asyncSetUp(self):
        self.client = HttpClient(os.getenv("API_TOKEN"))
        self.mock_get_patcher = patch(PATCH_OBJECT)
        self.mock_request = self.mock_get_patcher.start()

    async def asyncTearDown(self):
        self.mock_get_patcher.stop()
