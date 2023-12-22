from typing import Any

from client import (HttpClient, Request, RequestMessagesCreateData,
                    RequestMessagesUpdateData)
from routers import Router


class MessagesMethods:

    @classmethod
    async def send_messages(
        cls, client: HttpClient, data: dict[str, Any]
    ) -> dict[str, Any]:
        request: Request = Router.send_messages()
        request.data = {'message': RequestMessagesCreateData(data).to_dict()}
        return await client.make_request(request)

    @classmethod
    async def get_messages(cls, client: HttpClient) -> dict[str, Any]:
        request: Request = Router.get_messages()
        return await client.make_request(request)

    @classmethod
    async def get_message_by_id(
        cls, client: HttpClient, id: int
    ) -> dict[str, Any]:
        request: Request = Router.get_message_by_id(id)
        return await client.make_request(request)

    @classmethod
    async def edit_message(
        cls, client: HttpClient, id: int, data: dict[str, Any]
    ) -> dict[str, Any]:
        request: Request = Router.edit_message(id)
        request.data = {'message': RequestMessagesUpdateData(data).to_dict()}
        return await client.make_request(request)

    async def add_reaction(cls, *args, **kwargs):
        pass

    async def get_reaction(cls, *args, **kwargs):
        pass

    async def delete_reaction(cls, *args, **kwargs):
        pass

    async def create_threade(cls, *args, **kwargs):
        pass
