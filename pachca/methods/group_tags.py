from pachca.client import Request, HttpClient
from pachca.routers import Router


class GroupTagsMethods:

    @classmethod
    async def get_group_tags(cls, *args, client: HttpClient, **kwargs):
        request: Request = Router.get_group_tags()
        return await client.make_request(request)

    @classmethod
    async def get_group_tag_users(cls, *args, client: HttpClient, tag_id: int, **kwargs):
        request: Request = Router.get_group_tag_users(tag_id)
        return await client.make_request(request)
