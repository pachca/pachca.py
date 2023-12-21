from typing import Any, Dict, Optional

from pydantic import BaseModel


class Request(BaseModel):
    http_method: str = None
    url: str = None
    acceptable_statuses: tuple[int] = None
    data: Dict[str, Optional[Any]] = None


class RequestData(BaseModel):

    name: str = None
    member_ids: tuple[int] = None
    group_tag_ids: tuple[int] = None
    channel: bool = None
    public: bool = None

    def __init__(self, data: dict = None):
        super().__init__()
        if data is not None:
            for key, value in data.items():
                setattr(self, key, value)

    def to_dict(self):
        return self.__dict__
