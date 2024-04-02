from http import HTTPMethod, HTTPStatus

from pachca.client import Request

from pachca.routers.base import BaseRouter


class ChatsRouter(BaseRouter):

    __URL: str = 'chats/{id}'
    __URL_MEMBERS: str = 'chats/{id}/members'
    __URL_MEMBERS_DELETE: str = 'chats/{id}/members/{user_id}'
    __URL_TAGS: str = 'chats/{id}/group_tags'
    __URL_TAGS_DELETE: str = 'chats/{id}/group_tags/{tag_id}'

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
    def update_chat(cls, id: int) -> Request:
        return Request(
            url=cls._make_endpoint(cls.__URL).format(id=id),
            acceptable_statuses=(HTTPStatus.OK,),
            http_method=HTTPMethod.PUT.lower()
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

    @classmethod
    def delete_member_in_chat(cls, id: int, user_id: int) -> Request:
        return Request(
            url=cls._make_endpoint(cls.__URL_MEMBERS_DELETE).format(id=id, user_id=user_id),
            acceptable_statuses=(HTTPStatus.NO_CONTENT,),
            http_method=HTTPMethod.DELETE.lower()
        )

    @classmethod
    def delete_tags_in_chat(cls, id: int, tag_id: int) -> Request:
        return Request(
            url=cls._make_endpoint(cls.__URL_TAGS_DELETE).format(id=id, tag_id=tag_id),
            acceptable_statuses=(HTTPStatus.NO_CONTENT,),
            http_method=HTTPMethod.DELETE.lower()
        )
