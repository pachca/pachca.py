from pachca.client import HttpClient, Request, RequestData, TaskData
from pachca.routers import Router


class TasksMethods:

    @classmethod
    async def create_task(cls, *args, client: HttpClient, task: TaskData, **kwargs):
        request: Request = Router.create_task()
        request.data = RequestData(**task).to_dict()
        return await client.make_request(request)
