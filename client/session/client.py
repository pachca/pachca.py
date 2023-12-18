from aiohttp import ClientConnectionError

from .errors import WrongStatusError, ApiClientException
from .session import Session


BASE_URL = 'https://api.pachca.com/api/shared/v1/{postfix}'


class HttpClient:
    """HTTP API клиент."""

    """Может использоваться как асинхронный менеджер контекста."""

    def __init__(self, token=None, **kwargs):
        """Инициализируем клиент."""
        self._session = Session(token)

    async def _request(
            self, method, endpoint, data=None,
            acceptable_statuses=(200,)
    ):
        """Отправляет запрос к API."""
        session = await self._session.create_session()
        url = self._make_endpoint(endpoint)
        try:
            async with getattr(
                    session, method)(url=url, json=data) as response:
                await self._session.close()
                if response.status not in acceptable_statuses:
                    raise WrongStatusError(response.status)
                return await response.json()
        except (ConnectionError, TimeoutError, ClientConnectionError) as error:
            raise ApiClientException('Ошибка', error)

    def _make_endpoint(self, url) -> str:
        return BASE_URL.format(postfix=url)

    async def get(self, endpoint, acceptable_statuses=(200, )):
        """Отправляет GET-запрос."""
        return await self._request(
            "get", endpoint, acceptable_statuses=acceptable_statuses)

    async def post(self, endpoint, data, acceptable_statuses=(200, 201, 204)):
        """Отправляет POST-запрос."""
        return await self._request(
            "post", endpoint, data, acceptable_statuses=acceptable_statuses)

    async def patch(self, endpoint, data=None, acceptable_statuses=(200, 204)):
        """Отправляет PATCH-запрос."""
        return await self._request(
            "patch", endpoint, data, acceptable_statuses=acceptable_statuses)

    async def put(self, endpoint, data=None, acceptable_statuses=(200, 204)):
        """Отправляет PUT-запрос."""
        return await self._request(
            "put", endpoint, data, acceptable_statuses=acceptable_statuses)

    async def delete(self, endpoint, acceptable_statuses=(200, 204)):
        """Отправляет DELETE-запрос."""
        return await self._request(
            "delete", endpoint, acceptable_statuses=acceptable_statuses)
