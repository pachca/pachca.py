from pydantic import BaseModel


class ChatData(BaseModel):

    name: str
    public: bool = False


class TaskData(BaseModel):

    kind: str
    content: str = None
    due_at: str = None
    priority: int = None
    performer_ids: list[int] = None


class RequestData(BaseModel):

    task: TaskData = None
    chat: ChatData = None

    def __init__(self, data: dict = None):
        super().__init__()
        if data is not None:
            for key, value in data.items():
                setattr(self, key, value)

    def to_dict(self):
        return self.model_dump(exclude_none=True)


class Request(BaseModel):
    http_method: str = None
    url: str = None
    acceptable_statuses: tuple[int] = None
    data: RequestData = None
