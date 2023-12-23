from http import HTTPMethod, HTTPStatus

from client import Request
from .base import BaseRouter


class MessagesRouter(BaseRouter):

    URL_REACTIONS: str = 'messages/{id}/reactions'
    URL_THREAD: str = 'messages/{id}/thread'

    @classmethod
    def get_messages(cls, *args, **kwargs):
        pass

    @classmethod
    def get_message_by_id(cls, *args, **kwargs):
        pass

    @classmethod
    def edit_message(cls, *args, **kwargs):
        pass

    @classmethod
    def add_reaction(cls, id: int) -> Request:
        return Request(
            url=cls._make_endpoint(cls.URL_REACTIONS).format(id=id),
            acceptable_statuses=(HTTPStatus.CREATED,),
            http_method=HTTPMethod.POST.lower()
        )

    @classmethod
    def get_reactions(cls, id: int) -> Request:
        return Request(
            url=cls._make_endpoint(cls.URL_REACTIONS).format(id=id),
            acceptable_statuses=(HTTPStatus.OK,),
            http_method=HTTPMethod.GET.lower()
        )

    @classmethod
    def delete_reaction(cls, id: int) -> Request:
        return Request(
            url=cls._make_endpoint(cls.URL_REACTIONS).format(id=id),
            acceptable_statuses=(HTTPStatus.NO_CONTENT,),
            http_method=HTTPMethod.DELETE.lower()
        )

    @classmethod
    def send_messages(cls, *args, **kwargs):
        pass

    @classmethod
    def create_threade(cls, id: int) -> Request:
        return Request(
            url=cls._make_endpoint(cls.URL_THREAD).format(id=id),
            acceptable_statuses=(HTTPStatus.CREATED,),
            http_method=HTTPMethod.POST.lower()
        )
