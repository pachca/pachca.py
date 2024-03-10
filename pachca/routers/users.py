from http import HTTPMethod, HTTPStatus

from client import Request, HttpClient


class UserRouter(HttpClient):

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
            acceptable_statuses=(HTTPStatus.CREATED,),
            http_method=HTTPMethod.POST.lower()
        )
