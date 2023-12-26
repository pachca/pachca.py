from http import HTTPMethod, HTTPStatus

from client import Request

from .base import BaseRouter


class UploadsRouter(BaseRouter):

    URL_UPLOADS: str = 'uploads/'

    @classmethod
    def get_uploading_unique_params(cls) -> Request:
        return Request(
            url=cls._make_endpoint(cls.URL_UPLOADS),
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
