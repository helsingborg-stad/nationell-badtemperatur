from typing import Any

from pydantic import BaseModel


class BadTempGetResponseModel(BaseModel):
    data: Any
