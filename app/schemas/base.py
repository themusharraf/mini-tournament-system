from typing import Any, List, Optional

from pydantic import BaseModel


class BaseResponse(BaseModel):
    status: bool = True
    data: Optional[Any] = None
    errors: Optional[List[dict]] = None
