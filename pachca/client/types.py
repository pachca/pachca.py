from pydantic import BaseModel


class ChatData(BaseModel):

    name: str
    member_ids: tuple[int] = None
    group_tag_ids: tuple[int] = None
    channel: bool = None
    public: bool = None


class RequestData(BaseModel):

    chat: ChatData = None

    def to_dict(self):
        return self.model_dump(exclude_none=True)


class Request(BaseModel):
    http_method: str = None
    url: str = None
    acceptable_statuses: tuple[int] = None
    data: RequestData = None
