from http import HTTPMethod, HTTPStatus

from pachca.client import Request

from pachca.routers.base import BaseRouter


class UploadsRouter(BaseRouter):

    __URL: str = 'uploads/'

    @classmethod
    def uploads(cls) -> Request:
        return Request(
            url=cls._make_endpoint(cls.__URL),
            acceptable_statuses=(HTTPStatus.OK,),
            http_method=HTTPMethod.POST.lower()
        )

    @classmethod
    def upload_file(cls, upload_url: str) -> Request:
        return Request(
            url=upload_url,
            acceptable_statuses=(HTTPStatus.NO_CONTENT,),
            http_method=HTTPMethod.POST.lower()
        )
