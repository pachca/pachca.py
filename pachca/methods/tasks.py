from client import HttpClient, Request, RequestData
from routers import Router


class TasksMethods:

    @classmethod
    async def create_task(cls, client: HttpClient, data: dict):
        request: Request = Router.create_task()
        request.data = RequestData(data).to_dict()
        return await client.make_request(request)
