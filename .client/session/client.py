import asyncio

from aiohttp import ClientSession

BASE_URL = 'https://api.pachca.com/api/shared/v1/{postfix}'


class HttpClient:
    """HTTP API клиент."""

    """Может использоваться как асинхронный менеджер контекста."""

    def __init__(self, token=None):
        self.token = token
        self.session = None

    async def __aenter__(self):
        self.session = ClientSession(headers={"Authorization": f"Token {self.token}"})
        return self.session

    async def __aexit__(self, *args):
        await self.session.close()

    def _make_endpoint(self, url) -> str:
        return BASE_URL.format(postfix=url)
    
    async def _request(self, method, url, data=None, acceptable_statuses=(200,)):
        """Отправляет запрос к API."""
        url = self._make_endpoint(url)
        try:
            async with getattr(self.session, method)(url=url, json=data) as response:
                if response.status not in acceptable_statuses:
                    error_message = f"{method.upper()} request to {url=}, {data=} failed " f"with {response.status=}"
                    raise Exception(error_message)
                return await response.json()
        except (ConnectionError, TimeoutError,) as error:
            error_message = f"{method.upper()} to {url=} request failed due to a " f"connection error: {str(error)}"
            raise Exception(error_message)

    async def get(self, url, acceptable_statuses=(200,)):
        """Отправляет GET-запрос."""
        return await self._request("get", url, acceptable_statuses=acceptable_statuses)

    async def post(self, url, data, acceptable_statuses=(200, 201, 204)):
        """Отправляет POST-запрос."""
        return await self._request("post", url, data, acceptable_statuses=acceptable_statuses)

    async def put(self, url, data=None, acceptable_statuses=(200, 201, 204)):
        """Отправляет PATCH-запрос."""
        return await self._request("put", url, data, acceptable_statuses=acceptable_statuses)

    async def delete(self, url, data=None):
        return await self._request("delete", url, data)
