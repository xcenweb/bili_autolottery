from typing import Optional

from sqlalchemy import Integer, Text, text
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

class Base(DeclarativeBase):
    pass


class RepostUsersOld20250122(Base):
    __tablename__ = '_repost_users_old_20250122'

    name: Mapped[str] = mapped_column(Text)
    status: Mapped[str] = mapped_column(Text, server_default=text("'active'"))
    create_time: Mapped[str] = mapped_column(Text, server_default=text("strftime('%Y-%m-%d %H:%M:%S', 'now', 'localtime')"))
    update_time: Mapped[str] = mapped_column(Text, server_default=text("strftime('%Y-%m-%d %H:%M:%S', 'now', 'localtime')"))
    uid: Mapped[Optional[int]] = mapped_column(Integer, primary_key=True)
    face: Mapped[Optional[str]] = mapped_column(Text)
    level: Mapped[Optional[int]] = mapped_column(Integer, server_default=text('0'))


class UpUsersOld20250122(Base):
    __tablename__ = '_up_users_old_20250122'

    name: Mapped[str] = mapped_column(Text)
    create_time: Mapped[str] = mapped_column(Text, server_default=text("strftime('%Y-%m-%d %H:%M:%S', 'now', 'localtime')"))
    update_time: Mapped[str] = mapped_column(Text, server_default=text("strftime('%Y-%m-%d %H:%M:%S', 'now', 'localtime')"))
    uid: Mapped[Optional[int]] = mapped_column(Integer, primary_key=True)
    face: Mapped[Optional[str]] = mapped_column(Text)
    level: Mapped[Optional[int]] = mapped_column(Integer, server_default=text('0'))
    is_followed: Mapped[Optional[int]] = mapped_column(Integer, server_default=text('0'))


class LotteryDynamics(Base):
    __tablename__ = 'lottery_dynamics'

    dynamic_id: Mapped[int] = mapped_column(Integer)
    up_uid: Mapped[int] = mapped_column(Integer)
    type: Mapped[str] = mapped_column(Text)
    content: Mapped[str] = mapped_column(Text)
    publish_time: Mapped[str] = mapped_column(Text)
    status: Mapped[str] = mapped_column(Text, server_default=text("'pending'"))
    create_time: Mapped[str] = mapped_column(Text, server_default=text("strftime('%Y-%m-%d %H:%M:%S', 'now', 'localtime')"))
    update_time: Mapped[str] = mapped_column(Text, server_default=text("strftime('%Y-%m-%d %H:%M:%S', 'now', 'localtime')"))
    id: Mapped[Optional[int]] = mapped_column(Integer, primary_key=True)
    description: Mapped[Optional[str]] = mapped_column(Text)
    cover_image: Mapped[Optional[str]] = mapped_column(Text)
    view_count: Mapped[Optional[int]] = mapped_column(Integer, server_default=text('0'))
    like_count: Mapped[Optional[int]] = mapped_column(Integer, server_default=text('0'))
    comment_count: Mapped[Optional[int]] = mapped_column(Integer, server_default=text('0'))
    repost_count: Mapped[Optional[int]] = mapped_column(Integer, server_default=text('0'))
    prizes: Mapped[Optional[str]] = mapped_column(Text)
    conditions: Mapped[Optional[str]] = mapped_column(Text)
    require_level: Mapped[Optional[int]] = mapped_column(Integer, server_default=text('0'))
    require_days: Mapped[Optional[int]] = mapped_column(Integer, server_default=text('0'))
    due_time: Mapped[Optional[str]] = mapped_column(Text)


class RepostUsers(Base):
    __tablename__ = 'repost_users'

    name: Mapped[str] = mapped_column(Text)
    create_time: Mapped[str] = mapped_column(Text, server_default=text("strftime('%Y-%m-%d %H:%M:%S', 'now', 'localtime')"))
    update_time: Mapped[str] = mapped_column(Text, server_default=text("strftime('%Y-%m-%d %H:%M:%S', 'now', 'localtime')"))
    uid: Mapped[Optional[int]] = mapped_column(Integer, primary_key=True)
    face: Mapped[Optional[str]] = mapped_column(Text)
    level: Mapped[Optional[int]] = mapped_column(Integer, server_default=text('0'))


class UpUsers(Base):
    __tablename__ = 'up_users'

    name: Mapped[str] = mapped_column(Text)
    create_time: Mapped[str] = mapped_column(Text, server_default=text("strftime('%Y-%m-%d %H:%M:%S', 'now', 'localtime')"))
    update_time: Mapped[str] = mapped_column(Text, server_default=text("strftime('%Y-%m-%d %H:%M:%S', 'now', 'localtime')"))
    uid: Mapped[Optional[int]] = mapped_column(Integer, primary_key=True)
    face: Mapped[Optional[str]] = mapped_column(Text)
    level: Mapped[Optional[int]] = mapped_column(Integer, server_default=text('0'))
