from http import HTTPMethod, HTTPStatus

from pachca.client import Request

from pachca.routers.base import BaseRouter


class UsersRouter(BaseRouter):

    __URL: str = 'users/{id}'

    @classmethod
    def get_users(cls) -> Request:
        return Request(
            url=cls._make_endpoint(cls.__URL).format(id=''),
            acceptable_statuses=(HTTPStatus.OK,),
            http_method=HTTPMethod.GET.lower()
        )

    @classmethod
    def get_user_by_id(cls, id: int) -> Request:
        return Request(
            url=cls._make_endpoint(cls.__URL).format(id=id),
            acceptable_statuses=(HTTPStatus.OK,),
            http_method=HTTPMethod.GET.lower()
        )

    @classmethod
    def create_user(cls) -> Request:
        return Request(
            url=cls._make_endpoint(cls.__URL).format(id=''),
            acceptable_statuses=(HTTPStatus.OK,),
            http_method=HTTPMethod.POST.lower()
        )

    @classmethod
    def edit_user(cls, id: int) -> Request:
        return Request(
            url=cls._make_endpoint(cls.__URL).format(id=id),
            acceptable_statuses=(HTTPStatus.OK,),
            http_method=HTTPMethod.PUT.lower()
        )

    @classmethod
    def delete_user(cls, id: int) -> Request:
        return Request(
            url=cls._make_endpoint(cls.__URL).format(id=id),
            acceptable_statuses=(HTTPStatus.NO_CONTENT,),
            http_method=HTTPMethod.DELETE.lower()
        )
