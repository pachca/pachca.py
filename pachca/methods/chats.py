from client import HttpClient, Request, RequestData
from routers import Router


class ChatsMethods:

    @classmethod
    async def get_chats(cls, client: HttpClient):
        request: Request = Router.get_chats()
        return await client.make_request(request)

    @classmethod
    async def get_chat_by_id(cls, *args, **kwargs):
        pass

    @classmethod
    async def create_chat(cls, client: HttpClient, data: dict):
        request: Request = Router.create_chat()
        request.data = RequestData(**data).to_dict()
        return await client.make_request(request)

    @classmethod
    async def add_members_to_chat(cls, client: HttpClient, data: dict):
        request: Request = Router.add_members_to_chat()
        request.data = RequestData(data).to_dict()
        return await client.make_request(request)

    @classmethod
    async def add_tags_to_chat(cls, *args, **kwargs):
        pass
