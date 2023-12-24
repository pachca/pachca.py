from routers import Router
from client import HttpClient, Request


class UserMethods:

    @classmethod
    async def get_users(cls, client: HttpClient):
        request: Request = Router.get_users()
        return await client.make_request(request)

    @classmethod
    async def get_user_by_id(cls, client: HttpClient, id: int):
        request: Request = Router.get_user_by_id(id)
        return await client.make_request(request)
