import os
import unittest
from unittest.mock import patch

from pachca.bot import Bot


class TestBaseClient(unittest.IsolatedAsyncioTestCase):
    """Базовый класс тестирования."""

    async def asyncSetUp(self):
        self.bot = Bot(token=os.getenv("API_TOKEN"))
        self.mock_make_request = patch.object(self.bot.client, 'make_request')
        self.mock = self.mock_make_request.start()

    async def asyncTearDown(self):
        self.mock_make_request.stop()
