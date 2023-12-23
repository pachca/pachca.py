from client import HttpClient, Request, RequestData
from pydantic import ValidationError
from routers import Router


class MessagesMethods:

    async def get_messages(cls, *args, **kwargs):
        pass

    async def get_message_by_id(cls, *args, **kwargs):
        pass

    async def edit_message(cls, *args, **kwargs):
        pass

    @classmethod
    async def add_reaction(cls, id: int, client: HttpClient, data: dict):
        request: Request = Router.add_reaction(id)
        try:
            data: RequestData = RequestData(data)
        except ValidationError as error:
            raise error.errors()
        else:
            request.data = {data.to_dict()}
            return await client.make_request(request)

    @classmethod
    async def get_reactions(cls, id: int, client: HttpClient):
        request = Router.get_reactions(id)
        return await client.make_request(request)

    @classmethod
    async def delete_reaction(cls, id: int, client: HttpClient, data: dict):
        request: Request = Router.delete_reaction(id)
        try:
            data: RequestData = RequestData(data)
        except ValidationError as error:
            raise error.errors()
        else:
            request.data = {data.to_dict()}
            return await client.make_request(request)

    async def send_messages(cls, *args, **kwargs):
        pass

    @classmethod
    async def create_threade(cls, id: int, client: HttpClient):
        request = Router.create_threade(id)
        return await client.make_request(request)
