from typing import Any, Dict, Optional

from pydantic import BaseModel


class Request(BaseModel):
    http_method: str = None
    url: str = None
    acceptable_statuses: tuple[int] = None
    data: Dict[str, Optional[Any]] = None
