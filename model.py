from typing import Optional

from sqlalchemy import Integer, Text, text
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

class Base(DeclarativeBase):
    pass


class LotteryDynamics(Base):
    __tablename__ = 'lottery_dynamics'

    dynamic_id: Mapped[int] = mapped_column(Integer)
    up_uid: Mapped[int] = mapped_column(Integer)
    type: Mapped[str] = mapped_column(Text)
    content: Mapped[str] = mapped_column(Text)
    create_time: Mapped[str] = mapped_column(Text)
    status: Mapped[str] = mapped_column(Text, server_default=text("'pending'"))
    id: Mapped[Optional[int]] = mapped_column(Integer, primary_key=True)
    gift_list: Mapped[Optional[str]] = mapped_column(Text)
    due_time: Mapped[Optional[str]] = mapped_column(Text)
    auto_time: Mapped[Optional[str]] = mapped_column(Text)


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
