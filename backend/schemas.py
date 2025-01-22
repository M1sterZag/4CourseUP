from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class UserResponse(BaseModel):
    id: int
    username: str
    email: str
    avatar: Optional[str] = None
    is_premium: bool
    is_admin: bool
    created_at: datetime

    class Config:
        from_attributes = True


class GameResponse(BaseModel):
    id: int
    name: str
    avatar: Optional[str] = None
    max_people: int

    class Config:
        from_attributes = True


class ChatResponse(BaseModel):
    id: int
    name: str
    created_at: datetime

    class Config:
        from_attributes = True

class MessageResponse(BaseModel):
    id: int
    id_chat: int
    id_user: int
    text: str
    created_at: datetime
    id_parent: Optional[int] = None

    class Config:
        from_attributes = True

class PostResponse(BaseModel):
    id: int
    title: str
    content: str
    created_at: datetime

    class Config:
        from_attributes = True


class CommentResponse(BaseModel):
    id: int
    id_user: int
    id_post: int
    content: str
    created_at: datetime
    id_parent: Optional[int] = None

    class Config:
        from_attributes = True


class TeamResponse(BaseModel):
    id: int
    name: str
    id_chat: Optional[int]
    id_owner: int
    id_game: int
    description: Optional[str]
    count_people: int
    created_at: datetime
    time: datetime
    id_game_type: int

    class Config:
        from_attributes = True


class SubscriptionResponse(BaseModel):
    id: int
    name: str
    time: int
    price: float

    class Config:
        from_attributes = True