from typing import Optional, Union

from pydantic import BaseModel


class File(BaseModel):
    key: str
    name: str
    file_type: str
    size: int


class MessagesData(BaseModel):
    entity_type: Optional[str] = None
    entity_id: int = None
    parrent_message_id: Optional[int] = None
    content: str
    files: Union[Optional[list[File]], list[Optional[File]]] = None


class RequestData(BaseModel):
    message: MessagesData = None

    def to_dict(self):
        return self.model_dump(exclude_none=True)


class Request(BaseModel):
    http_method: str = None
    url: str = None
    acceptable_statuses: tuple[int] = None
    data: RequestData = None
