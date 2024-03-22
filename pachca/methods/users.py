from pachca.client import HttpClient, Request
from pachca.routers import Router


class UserMethods:

    @classmethod
    async def get_users(cls, *args, client: HttpClient, **kwargs):
        request: Request = Router.get_users()
        return await client.make_request(request)

    @classmethod
    async def get_user_by_id(cls, *args, client: HttpClient, id: int, **kwargs):
        request: Request = Router.get_user_by_id(id)
        return await client.make_request(request)
