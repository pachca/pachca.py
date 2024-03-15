from aiohttp import ClientConnectionError

from pachca.client.errors import ApiClientError, WrongStatusError
from pachca.client.session import Session
from pachca.client.types import Request


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
                session, request.http_method)(request.url, json=request.data,
                                              data=request.file_data)
            await self._session.close()
            if not response.content_length:
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
            raise ApiClientError('Ошибка подключения', error)
