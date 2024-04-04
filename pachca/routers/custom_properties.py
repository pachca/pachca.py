from http import HTTPMethod, HTTPStatus

from pachca.client import Request

from pachca.routers.base import BaseRouter


class CustomPropertiesRouter(BaseRouter):

    __URL: str = 'custom_properties/'

    @classmethod
    def get_custom_properties(cls) -> Request:
        return Request(
            url=cls._make_endpoint(cls.__URL),
            acceptable_statuses=(HTTPStatus.OK,),
            http_method=HTTPMethod.GET.lower()
        )
