from http import HTTPStatus, HTTPMethod

from client import Request
from .base import BaseRouter


class GroupTagsRouter(BaseRouter):

    __URL: str = 'group_tags/'
    __URL_ID: str = 'group_tags/{id}/users'

    @classmethod
    def group_tags(cls) -> Request:
        return Request(
            url=cls._make_endpoint(cls.__URL),
            acceptable_statuses=(HTTPStatus.OK,),
            http_method=HTTPMethod.GET.lower()
        )

    @classmethod
    def group_tag_users(cls, id: int) -> Request:
        return Request(
            url=cls._make_endpoint(cls.__URL_ID).format(id=id),
            acceptable_statuses=(HTTPStatus.OK,),
            http_method=HTTPMethod.GET.lower()
        )
