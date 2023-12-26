from aiohttp import ClientConnectionError

from .errors import ApiClientException, WrongStatusError
from .session import Session
from .types import Request


class HttpClient:
    """HTTP API клиент."""

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
            response = await getattr(
                session, request.http_method)(request.url, json=request.data)
                # session, request.http_method)(request.url, data=request.data)
            await self._session.close()
            if response.status not in request.acceptable_statuses:
                raise WrongStatusError(response.status)
            # if 'json' not in response.content_type:
            #     return None
            return await response.json()
        except (ConnectionError, TimeoutError, ClientConnectionError) as error:
            raise ApiClientException('Ошибка', error)
