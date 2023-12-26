from http import HTTPMethod, HTTPStatus

from client import Request
from .base import BaseRouter


class MessagesRouter(BaseRouter):

    __URL_CHAT_MESSAGES: str = (
        'messages/?chat_id={chat_id}&per={per}&page={page}'
    )
    __URL_MESSAGES: str = 'messages/{id}'
    __URL_REACTIONS: str = 'messages/{id}/reactions'
    __URL_THREAD: str = 'messages/{id}/thread'

    @classmethod
    def send_messages(cls) -> Request:
        return Request(
            url=cls._make_endpoint(cls.__URL_MESSAGES).format(id=''),
            acceptable_statuses=(HTTPStatus.CREATED,),
            http_method=HTTPMethod.POST.lower(),
        )

    @classmethod
    def get_messages(cls, chat_id, per, page) -> Request:
        return Request(
            url=cls._make_endpoint(cls.__URL_CHAT_MESSAGES).format(
                chat_id=chat_id, page=page, per=per
            ),
            acceptable_statuses=(HTTPStatus.OK,),
            http_method=HTTPMethod.GET.lower()
        )

    @classmethod
    def get_message_by_id(cls, id: int) -> Request:
        return Request(
            url=cls._make_endpoint(cls.__URL_MESSAGES).format(id=id),
            acceptable_statuses=(HTTPStatus.OK,),
            http_method=HTTPMethod.GET.lower()
        )

    @classmethod
    def edit_message(cls, id: int) -> Request:
        return Request(
            url=cls._make_endpoint(cls.__URL_MESSAGES).format(id=id),
            acceptable_statuses=(HTTPStatus.OK,),
            http_method=HTTPMethod.PUT.lower()
        )

    @classmethod
    def add_reaction(cls, id: int) -> Request:
        return Request(
            url=cls._make_endpoint(cls.__URL_REACTIONS).format(id=id),
            acceptable_statuses=(HTTPStatus.CREATED,),
            http_method=HTTPMethod.POST.lower()
        )

    @classmethod
    def get_reactions(cls, id: int) -> Request:
        return Request(
            url=cls._make_endpoint(cls.__URL_REACTIONS).format(id=id),
            acceptable_statuses=(HTTPStatus.OK,),
            http_method=HTTPMethod.GET.lower()
        )

    @classmethod
    def delete_reaction(cls, id: int) -> Request:
        return Request(
            url=cls._make_endpoint(cls.__URL_REACTIONS).format(id=id),
            acceptable_statuses=(HTTPStatus.NO_CONTENT,),
            http_method=HTTPMethod.DELETE.lower()
        )

    @classmethod
    def create_threade(cls, id: int) -> Request:
        return Request(
            url=cls._make_endpoint(cls.__URL_THREAD).format(id=id),
            acceptable_statuses=(HTTPStatus.CREATED,),
            http_method=HTTPMethod.POST.lower()
        )
