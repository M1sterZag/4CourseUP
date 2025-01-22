from sqlalchemy import Column, Integer, String, Boolean, Float, Text, DateTime, func, select, ForeignKey
from sqlalchemy.orm import declarative_base


Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(100), nullable=False, unique=True)
    email = Column(String(150), nullable=False, unique=True)
    password = Column(String(255), nullable=False)
    avatar = Column(Text, nullable=True)
    is_premium = Column(Boolean, default=False)
    created_at = Column(DateTime, server_default=func.now())
    is_admin = Column(Boolean, default=False)

class Game(Base):
    __tablename__ = 'games'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    avatar = Column(Text, nullable=True)
    max_people = Column(Integer, nullable=False, default=2)

class Chat(Base):
    __tablename__ = 'chat'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False, unique=True)
    created_at = Column(DateTime, server_default=func.now())

class ChatMember(Base):
    __tablename__ = 'chat_members'

    id = Column(Integer, primary_key=True, index=True)
    id_chat = Column(Integer, ForeignKey('chat.id'), nullable=False)
    id_user = Column(Integer, ForeignKey('users.id'), nullable=False)

class Message(Base):
    __tablename__ = 'message'

    id = Column(Integer, primary_key=True, index=True)
    id_chat = Column(Integer, ForeignKey('chat.id'), nullable=False)
    id_user = Column(Integer, ForeignKey('users.id'), nullable=False)
    text = Column(Text, nullable=False)
    created_at = Column(DateTime, server_default=func.now())
    id_parent = Column(Integer, ForeignKey('message.id'), nullable=True)

class Post(Base):
    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100), nullable=False)
    content = Column(Text, nullable=False)
    created_at = Column(DateTime, server_default=func.now())


class Tag(Base):
    __tablename__ = 'tags'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(40), nullable=False, unique=True)


class PostTag(Base):
    __tablename__ = 'post_tags'

    id = Column(Integer, primary_key=True, index=True)
    id_post = Column(Integer, ForeignKey('posts.id'), nullable=False)
    id_tag = Column(Integer, ForeignKey('tags.id'), nullable=False)


class Comment(Base):
    __tablename__ = 'comments'

    id = Column(Integer, primary_key=True, index=True)
    id_user = Column(Integer, ForeignKey('users.id'), nullable=False)
    id_post = Column(Integer, ForeignKey('posts.id'), nullable=False)
    content = Column(Text, nullable=False)
    created_at = Column(DateTime, server_default=func.now())
    id_parent = Column(Integer, ForeignKey('comments.id'), nullable=True)


class Team(Base):
    __tablename__ = 'teams'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False, unique=True)
    id_chat = Column(Integer, ForeignKey('chat.id'), unique=True, nullable=True)
    id_owner = Column(Integer, ForeignKey('users.id'), nullable=False)
    id_game = Column(Integer, ForeignKey('games.id'), nullable=False)
    description = Column(String(255), nullable=True)
    count_people = Column(Integer, default=1)
    created_at = Column(DateTime, server_default=func.now())
    time = Column(DateTime, nullable=False)
    id_game_type = Column(Integer, ForeignKey('game_types.id'), nullable=False)


class TeamMember(Base):
    __tablename__ = 'team_members'

    id = Column(Integer, primary_key=True, index=True)
    id_user = Column(Integer, ForeignKey('users.id'), nullable=False)
    id_team = Column(Integer, ForeignKey('teams.id'), nullable=False)
    joined_at = Column(DateTime, server_default=func.now())


class Subscription(Base):
    __tablename__ = 'subscriptions'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    time = Column(Integer, nullable=False)
    price = Column(Float, nullable=False)


class UserSubscription(Base):
    __tablename__ = 'user_subscriptions'

    id = Column(Integer, primary_key=True, index=True)
    id_user = Column(Integer, ForeignKey('users.id'), nullable=False)
    start_date = Column(DateTime, nullable=False)
    end_date = Column(DateTime, nullable=False)
    is_active = Column(Boolean, default=False)
    id_subscription = Column(Integer, ForeignKey('subscriptions.id'), nullable=False)