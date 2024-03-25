from pachca.client import HttpClient, Request, RequestData, ChatData
from pachca.routers import Router


class ChatsMethods:

    @classmethod
    async def get_chats(cls, *args, client: HttpClient, **kwargs):
        request: Request = Router.get_chats()
        return await client.make_request(request)

    @classmethod
    async def get_chat_by_id(cls, *args, client: HttpClient, id: int, **kwargs):
        request: Request = Router.get_chat_by_id(id)
        return await client.make_request(request)

    @classmethod
    async def create_chat(cls, *args, client: HttpClient, chat: ChatData, **kwargs):
        request: Request = Router.create_chat()
        request.data = RequestData(**chat).to_dict()
        return await client.make_request(request)

    @classmethod
    async def add_members_to_chat(
        cls,
        *args,
        client: HttpClient,
        id: int,
        member_ids: list[int],
        silent: bool = False,
        **kwargs,
    ):
        request: Request = Router.add_members_to_chat(id)
        kwargs = {}
        kwargs['member_ids'] = member_ids
        kwargs['silent'] = silent
        request.data = RequestData(**kwargs).to_dict()
        print(request)
        return await client.make_request(request)

    @classmethod
    async def add_tags_to_chat(cls, client: HttpClient, id: int, data: dict):
        request: Request = Router.add_tags_to_chat(id)
        request.data = RequestData(**data).to_dict()
        return await client.make_request(request)
