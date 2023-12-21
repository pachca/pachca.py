from aiohttp import ClientConnectionError

from .types import Request
from .session import Session
from .errors import WrongStatusError, ApiClientException


class HttpClient:
    """HTTP API клиент."""

    """Может использоваться как асинхронный менеджер контекста."""

    def __init__(self, token=None, **kwargs):
        """Инициализируем клиент."""
        self._session = Session(token)

    async def make_request(
            self,
            request: Request
    ):
        """Отправляет запрос к API."""
        session = await self._session.create_session()
        try:
            async with getattr(
                    session, request.http_method)(
                        request.url, json=request.data
                            ) as response:
                await self._session.close()
                if response.status not in request.acceptable_statuses:
                    raise WrongStatusError(response.status)
                return await response.json()
        except (ConnectionError, TimeoutError, ClientConnectionError) as error:
            raise ApiClientException('Ошибка', error)
