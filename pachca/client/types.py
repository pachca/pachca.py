from typing import Any, Optional

from pydantic import BaseModel


class File(BaseModel):
    key: str
    name: str
    file_type: str
    size: int


class ChatData(BaseModel):
    name: str
    public: Optional[bool] = False
    channel: Optional[bool] = False
    member_ids: Optional[list[int]] = None
    group_tag_ids: Optional[list[int]] = None


class MessagesData(BaseModel):
    entity_type: Optional[str] = None
    entity_id: int = None
    parrent_message_id: Optional[int] = None
    content: str
    files: Optional[list[File]] = None


class TaskData(BaseModel):
    kind: str
    content: Optional[str] = None
    due_at: Optional[str] = None
    priority: Optional[int] = None
    performer_ids: Optional[list[int]] = None


class RequestData(BaseModel):
    message: Optional[MessagesData] = None
    code: Optional[str] = None
    task: Optional[TaskData] = None
    chat: Optional[ChatData] = None
    member_ids: Optional[list[int]] = None
    group_tag_ids: Optional[list[int]] = None

    def to_dict(self):
        return self.model_dump(exclude_none=True)


class Request(BaseModel):
    http_method: str = None
    url: str = None
    acceptable_statuses: tuple[int] = None
    data: Optional[RequestData] = None
    file_data: Optional[dict[str, Any]] = None
