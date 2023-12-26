from typing import Optional

from pydantic import BaseModel


class ChatData(BaseModel):

    name: str
    public: Optional[bool] = False


class TaskData(BaseModel):

    kind: str
    content: Optional[str] = None
    due_at: Optional[str] = None
    priority: Optional[int] = None
    performer_ids: Optional[list[int]] = None


class RequestData(BaseModel):
    
    code: Optional[str] = None
    task: Optional[TaskData] = None
    chat: Optional[ChatData] = None

    def to_dict(self):
        return self.model_dump(exclude_none=True)


class Request(BaseModel):
    http_method: str = None
    url: str = None
    acceptable_statuses: tuple[int] = None
    data: Optional[RequestData] = None
