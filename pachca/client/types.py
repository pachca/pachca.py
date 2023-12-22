from typing import Any, Dict, Optional, Union

from pydantic import BaseModel


class Request(BaseModel):
    http_method: str = None
    url: str = None
    acceptable_statuses: tuple[int] = None
    data: Dict[str, Optional[Any]] = None


class BaseRequestData(BaseModel):
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


class File(BaseModel):
    key: str
    name: str
    file_type: str
    size: int


class RequestMessagesUpdateData(BaseRequestData):
    content: str
    files: list[Union[File, None]]


class RequestMessagesCreateData(BaseRequestData):
    entity_type: Optional[str] = 'discussion'
    entity_id: int
    parrent_message_id: Optional[int] = None
    content: str
    files: Optional[list[File]] = None
