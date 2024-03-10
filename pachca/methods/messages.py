from client import HttpClient, Request
from routers import Router


class MessagesMethods:

    @classmethod
    async def get_messages(
        cls, client: HttpClient, chat_id: int, per: int, page: int
    ):
        request: Request = Router.get_messages(chat_id, per, page)
        return await client.make_request(request)

    @classmethod
    async def get_message_by_id(
        cls, client: HttpClient, id: int
    ):
        request: Request = Router.get_message_by_id(id)
        return await client.make_request(request)

    @classmethod
    async def send_messages(
        cls, client: HttpClient,
        entity_type: str,
        entity_id: int,
        content: str,
        files: list[dict],
        parent_message_id: int
    ):
        request: Request = Router.send_messages()
        request.data = {
            'message': {
                'entity_type': entity_type,
                'entity_id': entity_id,
                'content': content,
                'files': files,
                'parent_message_id': parent_message_id
            }
        }
        return await client.make_request(request)

    @classmethod
    async def edit_message(
        cls, client: HttpClient,
        id: int,
        content: str,
        files: dict,
    ) -> dict:
        request: Request = Router.edit_message(id)
        request.data = {
            'message': {
                'content': content,
                'files': files
            }
        }
        return await client.make_request(request)

    @classmethod
    async def add_reaction(
        cls, client: HttpClient, message_id: int, code: str
    ):
        request: Request = Router.add_reaction(message_id)
        request.data = code
        return await client.make_request(request)

    @classmethod
    async def get_reactions(cls, id: int, client: HttpClient):
        request = Router.get_reactions(id)
        return await client.make_request(request)

    @classmethod
    async def delete_reaction(cls, id: int, client: HttpClient, code: str):
        request: Request = Router.delete_reaction(id)
        request.data = code
        return await client.make_request(request)

    @classmethod
    async def get_reactions(
        cls, client: HttpClient, chat_id: int, per: int, page: int
    ):
        request: Request = Router.get_reactions(per, page)
        return await client.make_request(request)

    @classmethod
    async def create_thread(cls, id: int, client: HttpClient):
        request = Router.create_thread(id)
        return await client.make_request(request)
