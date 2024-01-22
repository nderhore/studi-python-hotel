from typing import Optional

from pydantic import BaseModel


class AuthenticationSchema(BaseModel):
    username: str
    password: str


class AuthenticationSchemasBase(AuthenticationSchema):
    class Config:
        orm_mode = True


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Optional[str] = None
