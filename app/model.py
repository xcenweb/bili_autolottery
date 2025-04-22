from typing import Optional

from sqlalchemy import Integer, Text, text
from sqlalchemy.dialects.mysql import TEXT
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

class Base(DeclarativeBase):
    pass


class LotteryTasklists(Base):
    __tablename__ = 'lottery_tasklists'
    __table_args__ = {'comment': '抽奖任务表'}

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    dynamic_id: Mapped[Optional[int]] = mapped_column(Integer, comment='抽奖动态的id')
    user_id: Mapped[Optional[int]] = mapped_column(Integer, comment='抽奖up的id')
    method: Mapped[Optional[str]] = mapped_column(TEXT, comment='抽奖方式')
    content: Mapped[Optional[str]] = mapped_column(TEXT, comment='动态内容')
    status: Mapped[Optional[str]] = mapped_column(TEXT, comment='执行状态：executing/complete/error')
    gift_list: Mapped[Optional[str]] = mapped_column(TEXT, comment='奖品列表')
    due_time: Mapped[Optional[str]] = mapped_column(TEXT, comment='抽奖过期时间')
    auto_time: Mapped[Optional[str]] = mapped_column(TEXT, comment='任务计划时间')
    create_time: Mapped[Optional[str]] = mapped_column(TEXT, comment='创建时间')


class RepostDynamics(Base):
    __tablename__ = 'repost_dynamics'
    __table_args__ = {'comment': '用户转发的动态表'}

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    dyn_id: Mapped[Optional[int]] = mapped_column(Integer, comment='抽奖动态id')
    up_id: Mapped[Optional[int]] = mapped_column(Integer, comment='发布抽奖up的id')
    repost_dyn_id: Mapped[Optional[int]] = mapped_column(Integer, comment='转发动态id')
    reposter_id: Mapped[Optional[int]] = mapped_column(Integer, comment='转发者用户id')
    method: Mapped[Optional[str]] = mapped_column(TEXT, comment='抽奖方式')
    content: Mapped[Optional[str]] = mapped_column(TEXT, comment='动态内容')
    gift_list: Mapped[Optional[str]] = mapped_column(TEXT, comment='奖品列表')
    is_process: Mapped[Optional[str]] = mapped_column(TEXT, comment='是否已被处理过')
    due_time: Mapped[Optional[str]] = mapped_column(TEXT, comment='抽奖过期时间')
    create_time: Mapped[Optional[str]] = mapped_column(TEXT, comment='录入时间')


class Users(Base):
    __tablename__ = 'users'
    __table_args__ = {'comment': '用户信息表'}

    user_id: Mapped[int] = mapped_column(Integer, primary_key=True, comment='用户id')
    name: Mapped[str] = mapped_column(TEXT, comment='名称')
    level: Mapped[Optional[int]] = mapped_column(Integer, server_default=text("'0'"), comment='等级')
    face: Mapped[Optional[str]] = mapped_column(TEXT, comment='头像')
    type: Mapped[Optional[str]] = mapped_column(TEXT, comment='用户类型：up/reposter')
    create_time: Mapped[Optional[str]] = mapped_column(Text(collation='utf8mb4_general_ci'), comment='记录时间')
    update_time: Mapped[Optional[str]] = mapped_column(Text(collation='utf8mb4_general_ci'), comment='更新时间')
