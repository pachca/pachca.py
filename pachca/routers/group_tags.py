from http import HTTPStatus, HTTPMethod

from pachca.client import Request
from pachca.routers.base import BaseRouter


class GroupTagsRouter(BaseRouter):

    __URL: str = 'group_tags/'
    __URL_ID: str = 'group_tags/{id}/users'

    @classmethod
    def get_group_tags(cls) -> Request:
        return Request(
            url=cls._make_endpoint(cls.__URL),
            acceptable_statuses=(HTTPStatus.OK,),
            http_method=HTTPMethod.GET.lower()
        )

    @classmethod
    def get_group_tag_users(cls, id: int) -> Request:
        return Request(
            url=cls._make_endpoint(cls.__URL_ID).format(id=id),
            acceptable_statuses=(HTTPStatus.OK,),
            http_method=HTTPMethod.GET.lower()
        )
