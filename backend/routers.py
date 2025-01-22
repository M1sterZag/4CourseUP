from models import Chat, Comment, Game, Message, Post, Subscription, Team, User
from schemas import ChatResponse, CommentResponse, GameResponse, MessageResponse, PostResponse, SubscriptionResponse, TeamResponse, UserResponse
from fastapi import APIRouter, Depends
from db import AsyncSession, get_db
from sqlalchemy import select

router = APIRouter()

@router.get("/users/", response_model=list[UserResponse])
async def get_all_users(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(User))
    users = result.scalars().all()
    return [
        UserResponse(
            id=user.id,
            username=user.username,
            email=user.email,
            avatar=user.avatar,
            is_premium=user.is_premium,
            is_admin=user.is_admin,
            created_at=user.created_at
        ) for user in users
    ]

@router.get("/games/", response_model=list[GameResponse])
async def get_all_games(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Game))
    games = result.scalars().all()
    return [
        GameResponse(
            id=game.id,
            name=game.name,
            avatar=game.avatar,
            max_people=game.max_people
        ) for game in games
    ]

@router.get("/chats/", response_model=list[ChatResponse])
async def get_all_chats(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Chat))
    chats = result.scalars().all()
    return [
        ChatResponse(
            id=chat.id,
            name=chat.name,
            created_at=chat.created_at
        ) for chat in chats
    ]

@router.get("/messages/", response_model=list[MessageResponse])
async def get_all_messages(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Message))
    messages = result.scalars().all()
    return [
        MessageResponse(
            id=message.id,
            id_chat=message.id_chat,
            id_user=message.id_user,
            text=message.text,
            created_at=message.created_at,
            id_parent=message.id_parent
        ) for message in messages
    ]

@router.get("/posts/", response_model=list[PostResponse])
async def get_all_posts(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Post))
    posts = result.scalars().all()
    return [
        PostResponse(
            id=post.id,
            title=post.title,
            content=post.content,
            created_at=post.created_at
        ) for post in posts
    ]


@router.get("/comments/", response_model=list[CommentResponse])
async def get_all_comments(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Comment))
    comments = result.scalars().all()
    return [
        CommentResponse(
            id=comment.id,
            id_user=comment.id_user,
            id_post=comment.id_post,
            content=comment.content,
            created_at=comment.created_at,
            id_parent=comment.id_parent
        ) for comment in comments
    ]


@router.get("/teams/", response_model=list[TeamResponse])
async def get_all_teams(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Team))
    teams = result.scalars().all()
    return [
        TeamResponse(
            id=team.id,
            name=team.name,
            id_chat=team.id_chat,
            id_owner=team.id_owner,
            id_game=team.id_game,
            description=team.description,
            count_people=team.count_people,
            created_at=team.created_at,
            time=team.time,
            id_game_type=team.id_game_type
        ) for team in teams
    ]


@router.get("/subscriptions/", response_model=list[SubscriptionResponse])
async def get_all_subscriptions(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Subscription))
    subscriptions = result.scalars().all()
    return [
        SubscriptionResponse(
            id=subscription.id,
            name=subscription.name,
            time=subscription.time,
            price=subscription.price
        ) for subscription in subscriptions
    ]