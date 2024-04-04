from pachca.client import HttpClient, Request, RequestData, TaskData
from pachca.routers import Router


class TasksMethods:

    @classmethod
    async def create_task(cls, *args, client: HttpClient, task_data: TaskData, **kwargs):
        request: Request = Router.create_task()
        request.data = RequestData(task=task_data).to_dict()
        return await client.make_request(request)
