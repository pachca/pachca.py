from pachca.client import HttpClient, Request, RequestData, MessagesData

from pachca.routers import Router


class MessagesMethods:

    @classmethod
    async def send_messages(
        cls, *args, client: HttpClient, message: MessagesData, **kwargs
    ) -> dict:
        request: Request = Router.send_messages()
        request.data = RequestData(**message).to_dict()
        return await client.make_request(request)

    @classmethod
    async def get_messages(
        cls, *args, client: HttpClient, chat_id: int, per: int, page: int, **kwargs
    ) -> dict:
        request: Request = Router.get_messages(chat_id, per, page)
        return await client.make_request(request)

    @classmethod
    async def get_message_by_id(
        cls, *args, client: HttpClient, id: int, **kwargs
    ) -> dict:
        request: Request = Router.get_message_by_id(id)
        return await client.make_request(request)

    @classmethod
    async def edit_message(
        cls, *args, client: HttpClient, id: int, message: MessagesData, **kwargs
    ) -> dict:
        request: Request = Router.edit_message(id)
        request.data = RequestData(**message).to_dict()
        return await client.make_request(request)

    @classmethod
    async def add_reaction(cls, *args, client: HttpClient, id: int, code: str, **kwargs):
        request: Request = Router.add_reaction(id)
        kwargs['code'] = code
        request.data: RequestData = RequestData(**kwargs).to_dict()
        return await client.make_request(request)

    @classmethod
    async def get_reactions(cls, id: int, client: HttpClient):
        request = Router.get_reactions(id)
        return await client.make_request(request)

    @classmethod
    async def delete_reaction(cls, id: int, client: HttpClient, data: dict):
        request: Request = Router.delete_reaction(id)
        request.data: RequestData = RequestData(**data).to_dict()
        return await client.make_request(request)

    @classmethod
    async def create_thread(cls, id: int, client: HttpClient):
        request = Router.create_thread(id)
        return await client.make_request(request)
