from typing import Any, Optional

from pydantic import BaseModel


class Request(BaseModel):
    http_method: str = None
    # chunked: bool = False
    url: str = None
    acceptable_statuses: tuple[int] = None
    data: Optional[dict] = None
    file_data: Optional[dict[str, Any]] = None

    # def __init__(self, **data):
    #     super().__init__(**data)
    #     if self.http_method == HTTPMethod.GET.lower():
    #         self.chunked = True
