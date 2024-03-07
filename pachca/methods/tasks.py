from client import HttpClient, Request
from routers import Router


class TasksMethods:

    @classmethod
    async def create_task(
        cls,
        client: HttpClient,
        kind: str,
        content: str,
        due_at: str,
        priority: int,
        performer_ids: list[int]
    ):
        request: Request = Router.create_task()
        request.data = {
            'task': {
                'kind': kind,
                'content': content,
                'due_at': due_at,
                'priority': priority,
                'performer_ids': performer_ids
            }
        }
        return await client.make_request(request)
