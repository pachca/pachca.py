from http import HTTPMethod, HTTPStatus

from pachca.client import Request
from pachca.routers.base import BaseRouter


class TasksRouter(BaseRouter):

    __URL: str = 'tasks/'

    @classmethod
    def create_task(cls) -> Request:
        return Request(
            url=cls._make_endpoint(cls.__URL),
            acceptable_statuses=(HTTPStatus.CREATED,),
            http_method=HTTPMethod.POST.lower()
        )
