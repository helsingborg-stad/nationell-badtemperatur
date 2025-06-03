from pydantic import BaseModel


class BadTempPostResponseModel(BaseModel):
    received: bool
