import asyncio
import os

from dotenv import load_dotenv

from session import HttpClient
from methods import get_users


load_dotenv()


class Bot:
    """
    Bot class.
    """

    def __init__(self, token=None):
        self.client = HttpClient(token)

    async def get_users(self):
        """Method for getting a list of employees. Requires no parameters."""
        return await get_users(self.client)


async def main():
    token = os.getenv('TOKEN')
    bot = Bot(token=token)
    resp = await bot.get_users()
    print(resp)

asyncio.run(main())
