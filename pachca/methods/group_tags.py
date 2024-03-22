from pachca.client import Request, HttpClient
from pachca.routers import Router


class GroupTagsMethods:

    @classmethod
    async def get_group_tags(cls, *args, **kwargs):
        client: HttpClient = kwargs.get('client')
        request: Request = Router.get_group_tags()
        return await client.make_request(request)

    @classmethod
    async def get_group_tag_users(cls, *args, tag_id: int, **kwargs):
        client: HttpClient = kwargs.get('client')
        request: Request = Router.get_group_tag_users(tag_id)
        return await client.make_request(request)
