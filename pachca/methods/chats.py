from client import HttpClient, Request
from routers import Router


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
    async def create_chat(
        cls, client: HttpClient,
            name: str,
            member_ids: list[int] = None,
            group_tag_ids: list[int] = None,
            channel: bool = False,
            public: bool = False
    ):
        request: Request = Router.create_chat()
        request.data = {
            'chat': {
                'name': name,
                'member_ids': member_ids,
                'group_tag_ids': group_tag_ids,
                'channel': channel,
                'public': public
            }
        }
        return await client.make_request(request)

    @classmethod
    async def add_members_to_chat(
        cls,
        client: HttpClient,
        id: int,
        member_ids: list[int],
        silent: bool
    ):
        request: Request = Router.add_members_to_chat(id)
        request.data = {
            'member_ids': member_ids,
            'silent': silent
        }
        return await client.make_request(request)

    @classmethod
    async def add_tags_to_chat(
        cls,
        client: HttpClient,
        id: int, group_tag_ids: list[int]
    ):
        request: Request = Router.add_tags_to_chat(id)
        request.data = {
            'group_tag_ids': group_tag_ids
        }
        return await client.make_request(request)
