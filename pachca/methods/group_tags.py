from client import HttpClient, Request
from routers import Router


class GroupTagsMethods:

    @classmethod
    async def list_group_tags(cls, client: HttpClient):
        request: Request = Router.group_tags()
        return await client.make_request(request)

    @classmethod
    async def list_tag_users(cls, client: HttpClient, tag_id: int):
        request: Request = Router.group_tag_users(tag_id)
        return await client.make_request(request)
