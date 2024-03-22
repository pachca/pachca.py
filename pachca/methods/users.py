from pachca.client import HttpClient, Request
from pachca.routers import Router


class UserMethods:

    @classmethod
    async def get_users(cls, *args, **kwargs):
        client: HttpClient = kwargs.get('client')
        request: Request = Router.get_users()
        return await client.make_request(request)

    @classmethod
    async def get_user_by_id(cls, *args, id: int, **kwargs):
        client: HttpClient = kwargs.get('client')
        request: Request = Router.get_user_by_id(id)
        return await client.make_request(request)
