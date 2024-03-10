from aiohttp import ClientConnectionError

from .errors import ApiClientException
from .session import Session
from .types import Request


class HttpClient:
    """HTTP API клиент."""

    BASE_URL = 'https://api.pachca.com/api/shared/v1/{postfix}'

    def __init__(self, token=None, **kwargs):
        """Инициализируем клиент."""
        self._session = Session(token)

    @classmethod
    def _make_endpoint(cls, url) -> str:
        return cls.BASE_URL.format(postfix=url)

    async def make_request(
            self,
            request: Request
    ):
        """Отправляет запрос к API."""
        session = await self._session.create_session()
        try:
            response = await getattr(
                session, request.http_method)(
                    request.url,
                    json=request.data,
                    data=request.file_data
            )
            await self._session.close()
            content = await response.content.read()
            if not content:
                return ''

            return content.decode('utf-8')
        except (ConnectionError, TimeoutError, ClientConnectionError) as error:
            raise ApiClientException('Ошибка подключения', error)
