from client import HttpClient, Request, RequestData

from routers import Router


class MessagesMethods:

    @classmethod
    async def send_messages(
        cls, client: HttpClient, data: dict
    ) -> dict:
        request: Request = Router.send_messages()
        request.data = RequestData(**data).to_dict()
        return await client.make_request(request)

    @classmethod
    async def get_messages(
        cls, client: HttpClient, chat_id: int, per: int, page: int
    ) -> dict:
        request: Request = Router.get_messages(chat_id, per, page)
        return await client.make_request(request)

    @classmethod
    async def get_message_by_id(
        cls, client: HttpClient, id: int
    ) -> dict:
        request: Request = Router.get_message_by_id(id)
        return await client.make_request(request)

    @classmethod
    async def edit_message(
        cls, client: HttpClient, id: int, data: dict
    ) -> dict:
        request: Request = Router.edit_message(id)
        request.data = RequestData(**data).to_dict()
        return await client.make_request(request)

    @classmethod
    async def add_reaction(cls, client: HttpClient, id: int, data: dict):
        request: Request = Router.add_reaction(id)
        request.data: RequestData = RequestData(**data).to_dict()
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
    async def create_threade(cls, id: int, client: HttpClient):
        request = Router.create_threade(id)
        return await client.make_request(request)
