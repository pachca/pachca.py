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
    async def create_chat(cls, *args, client: HttpClient, chat_data: ChatData, **kwargs):
        request: Request = Router.create_chat()
        request.data = RequestData(chat_data=chat_data).to_dict()
        return await client.make_request(request)

    @classmethod
    async def update_chat(cls, *args, client: HttpClient, id: int, chat_data: ChatData, **kwargs):
        request: Request = Router.update_chat(id)
        request.data = RequestData(chat=chat_data).to_dict()
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
        request.data = RequestData(
            member_ids=member_ids,
            silent=silent,
        ).to_dict()
        print(request)
        return await client.make_request(request)

    @classmethod
    async def add_tags_to_chat(cls, *args, client: HttpClient, id: int, group_tag_ids: list[int], **kwargs):
        request: Request = Router.add_tags_to_chat(id)
        request.data = RequestData(group_tag_ids=group_tag_ids).to_dict()
        return await client.make_request(request)

    @classmethod
    async def delete_member_in_chat(cls, *args, client: HttpClient, id: int, member_id: int, **kwargs):
        request: Request = Router.delete_member_in_chat(id=id, user_id=member_id)
        return await client.make_request(request)

    @classmethod
    async def delete_tag_in_chat(cls, *args, client: HttpClient, id: int, group_tag_id: int, **kwargs):
        request: Request = Router.delete_tags_in_chat(id=id, tag_id=group_tag_id)
        return await client.make_request(request)
