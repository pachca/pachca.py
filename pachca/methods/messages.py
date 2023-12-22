from routers import Router
from client import BaseRequestData, Request, RequestReactionData, HttpClient
from pydantic import ValidationError


class MessagesMethods:

    async def get_messages(cls, *args, **kwargs):
        pass

    async def get_message_by_id(cls, *args, **kwargs):
        pass

    async def edit_message(cls, *args, **kwargs):
        pass

    @classmethod
    async def add_reaction(cls, id: int, client: HttpClient, data: dict):
        request: Request = Router.delete_reaction(id)
        try:
            data: BaseRequestData = RequestReactionData(data)
        except ValidationError as e:
            raise e.errors()
        else:
            request.data = {'code': data.to_dict()}
            return await client.make_request(request)

    @classmethod
    async def get_reactions(cls, id: int, client: HttpClient):
        request = Router.get_reactions(id)
        return await client.make_request(request)

    @classmethod
    async def delete_reaction(cls, id: int, client: HttpClient, data: dict):
        request: Request = Router.delete_reaction(id)
        try:
            data: BaseRequestData = RequestReactionData(data)
        except ValidationError as e:
            raise e.errors()
        else:
            request.data = {'code': data.to_dict()}
            return await client.make_request(request)

    async def send_messages(cls, *args, **kwargs):
        pass

    @classmethod
    async def create_threade(cls, id: int, client: HttpClient):
        request = Router.create_threade(id)
        return await client.make_request(request)
