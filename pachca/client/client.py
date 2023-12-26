from aiohttp import ClientConnectionError
from http import HTTPStatus

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
                session, request.http_method)(
                    request.url, json=request.data)
            await self._session.close()
            if response.status == HTTPStatus.NO_CONTENT:
                return ''
            resp_json = await response.json()
            if response.status not in request.acceptable_statuses:
                message = ', '.join(
                    [error['message'] for error in resp_json['errors']]
                )
                raise WrongStatusError({
                    'status': response.status,
                    'message': message
                })
            return resp_json
        except (ConnectionError, TimeoutError, ClientConnectionError) as error:
            raise ApiClientException('Ошибка подключения', error)
