import json
from aiohttp import ClientSession, ClientConnectionError

from .errors import ApiClientError, WrongStatusError
from .types import Request


class HttpClient:
    def __init__(self, token):
        self._token = token

    async def make_request(self, request: Request):
        """Отправляет запрос к API."""
        try:
            async with ClientSession(headers={'Authorization': f'Bearer {self._token}'}) as session:
                async with getattr(session, request.http_method)(request.url, json=request.data, data=request.file_data) as response:

                    data = await response.content.read()
                    try:
                        response_json = json.loads(data)
                    except Exception:
                        return None

                    if response.status not in request.acceptable_statuses:
                        message = ', '.join([error['message'] for error in response_json['errors']])
                        raise WrongStatusError({
                            'status': response.status,
                            'message': message
                        })

                    return response_json
        except (ConnectionError, TimeoutError, ClientConnectionError) as error:
            raise ApiClientError('Ошибка подключения', error)
