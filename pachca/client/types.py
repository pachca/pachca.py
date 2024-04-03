from typing import Any, Optional
from enum import Enum

from pydantic import BaseModel


class FileType(str, Enum):
    FILE = 'file'
    IMAGE = 'image'


class File(BaseModel):
    key: str
    name: str
    file_type: FileType
    size: int


class CustomProperties(BaseModel, extra='allow'):
    id: Optional[int] = None
    value: Optional[str] = None


class ChatData(BaseModel):
    name: Optional[str] = None
    public: Optional[bool] = False
    channel: Optional[bool] = False
    member_ids: Optional[list[int]] = None
    group_tag_ids: Optional[list[int]] = None


class MessagesData(BaseModel):
    entity_type: Optional[str] = None
    entity_id: int = None
    parrent_message_id: Optional[int] = None
    content: str = None
    files: Optional[list[File]] = None


class TaskData(BaseModel):
    kind: str
    content: Optional[str] = None
    due_at: Optional[str] = None
    priority: Optional[int] = None
    performer_ids: Optional[list[int]] = None


class UserData(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    nickname: Optional[str] = None
    email: Optional[str] = None
    phone_number: Optional[str] = None
    department: Optional[str] = None
    role: Optional[str] = None
    suspended: Optional[str] = None
    list_tags: Optional[list[str]] = None
    custom_properties: Optional[CustomProperties] = None
    skip_email_notify: Optional[bool] = False


class RequestData(BaseModel):
    user: Optional[UserData] = None
    entity_type: Optional[str] = None
    message: Optional[MessagesData] = None
    code: Optional[str] = None
    silent: Optional[bool] = False
    task: Optional[TaskData] = None
    chat: Optional[ChatData] = None
    member_ids: Optional[list[int]] = None
    group_tag_ids: Optional[list[int]] = None

    def to_dict(self):
        return self.model_dump(exclude_none=True)


class Request(BaseModel):
    http_method: str
    url: str
    acceptable_statuses: tuple[int] = None
    data: Optional[RequestData] = None
    file_data: Optional[dict[str, Any]] = None
