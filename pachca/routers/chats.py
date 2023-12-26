from http import HTTPMethod, HTTPStatus

from client import Request

from .base import BaseRouter


class ChatsRouter(BaseRouter):

    __URL: str = 'chats/{id}'

    @classmethod
    def get_chats(cls) -> Request:
        return Request(
            url=cls._make_endpoint(cls.__URL).format(id=''),
            acceptable_statuses=(HTTPStatus.OK,),
            http_method=HTTPMethod.GET.lower()
        )

    @classmethod
    def get_chat_by_id(cls, id: int) -> Request:
        return Request(
            url=cls._make_endpoint(cls.__URL).format(id=id),
            acceptable_statuses=(HTTPStatus.OK,),
            http_method=HTTPMethod.GET.lower()
        )

    @classmethod
    def create_chat(cls) -> Request:
        return Request(
            url=cls._make_endpoint(cls.__URL).format(id=''),
            acceptable_statuses=(HTTPStatus.CREATED,),
            http_method=HTTPMethod.POST.lower()
        )

    @classmethod
    def add_members_to_chat(cls, id: int) -> Request:
        return Request(
            url=cls._make_endpoint(cls.__URL).format(id=id),
            acceptable_statuses=(HTTPStatus.CREATED,),
            http_method=HTTPMethod.POST.lower()
        )

    @classmethod
    def add_tags_to_chat(cls, id: int) -> Request:
        return Request(
            url=cls._make_endpoint(cls.__URL).format(id=id),
            acceptable_statuses=(HTTPStatus.CREATED,),
            http_method=HTTPMethod.POST.lower()
        )
