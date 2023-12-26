from client import HttpClient, Request
from routers import Router


class GroupTagsMethods:

    @classmethod
    async def get_group_tags(cls, client: HttpClient):
        request: Request = Router.get_group_tags()
        return await client.make_request(request)

    @classmethod
    async def get_group_tag_users(cls, client: HttpClient, tag_id: int):
        request: Request = Router.get_group_tag_users(tag_id)
        return await client.make_request(request)
