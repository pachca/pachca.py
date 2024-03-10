from http import HTTPMethod, HTTPStatus

from client import Request, HttpClient


class TasksRouter(HttpClient):

    __URL: str = 'tasks/'

    @classmethod
    def create_task(cls) -> Request:
        return Request(
            url=cls._make_endpoint(cls.__URL),
            acceptable_statuses=(HTTPStatus.CREATED,),
            http_method=HTTPMethod.POST.lower()
        )
