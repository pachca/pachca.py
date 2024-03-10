from http import HTTPMethod, HTTPStatus

from client import HttpClient, Request


class ChatsRouter(HttpClient):

    __URL: str = 'chats/{id}'
    __URL_MEMBERS: str = 'chats/{id}/members'
    __URL_TAGS: str = 'chats/{id}/group_tags'

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
            url=cls._make_endpoint(cls.__URL_MEMBERS).format(id=id),
            acceptable_statuses=(HTTPStatus.CREATED,),
            http_method=HTTPMethod.POST.lower()
        )

    @classmethod
    def add_tags_to_chat(cls, id: int) -> Request:
        return Request(
            url=cls._make_endpoint(cls.__URL_TAGS).format(id=id),
            acceptable_statuses=(HTTPStatus.CREATED,),
            http_method=HTTPMethod.POST.lower()
        )
