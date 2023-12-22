from client import HttpClient, Request
from routers import Router


class UserMethods:

    @classmethod
    async def get_users(cls, client: HttpClient):
        request: Request = Router.get_users()
        return await client.make_request(request)

    @classmethod
    async def get_user_by_id(cls, id: int):
        pass

    @classmethod
    async def create_user(cls, data):
        pass
