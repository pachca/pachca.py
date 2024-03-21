from pachca.client import HttpClient, Request, RequestData
from pachca.routers import Router


class ChatsMethods:

    @classmethod
    async def get_chats(cls, client: HttpClient):
        request: Request = Router.get_chats()
        return await client.make_request(request)

    @classmethod
    async def get_chat_by_id(cls, client: HttpClient, id: int):
        request: Request = Router.get_chat_by_id(id)
        return await client.make_request(request)

    @classmethod
    async def create_chat(cls, client: HttpClient, **data):
        request: Request = Router.create_chat()
        data['chat'] = data
        request.data = RequestData(**data).to_dict()
        return await client.make_request(request)

    @classmethod
    async def add_members_to_chat(
        cls,
        client: HttpClient,
        id: int,
        data: dict
    ):
        request: Request = Router.add_members_to_chat(id)
        request.data = RequestData(**data).to_dict()
        return await client.make_request(request)

    @classmethod
    async def add_tags_to_chat(cls, client: HttpClient, id: int, data: dict):
        request: Request = Router.add_tags_to_chat(id)
        request.data = RequestData(**data).to_dict()
        return await client.make_request(request)
