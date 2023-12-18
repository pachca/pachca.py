import asyncio

from aiohttp import ClientSession


class Session:

    def __init__(self, token=None, **kwargs):
        self.token = token
        self._session = None

    async def create_session(self):
        if self._session is None or self._session.closed:
            self._session = ClientSession(
                headers={
                    "Authorization": f"Bearer {self.token}",
                },
            )
        return self._session

    async def close(self):
        if self._session is not None and not self._session.closed:
            await self._session.close()
            await asyncio.sleep(0.25)

    async def __aenter__(self):
        await self.create_session()
        return self

    async def __aexit__(self, exc_type, exc, tb):
        await self._session.close()
        await asyncio.sleep(0.25)
