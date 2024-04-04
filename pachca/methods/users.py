from pachca.client import HttpClient, Request, RequestData, UserData
from pachca.routers import Router


class UsersMethods:

    @classmethod
    async def get_users(cls, *args, client: HttpClient, **kwargs):
        request: Request = Router.get_users()
        return await client.make_request(request)

    @classmethod
    async def get_user_by_id(cls, *args, client: HttpClient, id: int, **kwargs):
        request: Request = Router.get_user_by_id(id)
        return await client.make_request(request)

    @classmethod
    async def create_user(cls, *args, client: HttpClient, user_data: UserData, **kwargs):
        request: Request = Router.create_user()
        request.data = RequestData(user=user_data).to_dict()
        return await client.make_request(request)

    @classmethod
    async def edit_user(cls, *args, client: HttpClient, id: int, user_data: UserData, **kwargs):
        request: Request = Router.edit_user(id)
        request.data = RequestData(user=user_data).to_dict()
        return await client.make_request(request)

    @classmethod
    async def delete_user(cls, *args, client: HttpClient, id: int, **kwargs):
        request: Request = Router.delete_user(id)
        return await client.make_request(request)
