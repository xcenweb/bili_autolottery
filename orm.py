from typing import Optional

from sqlalchemy import Integer
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

class Base(DeclarativeBase):
    pass


class DynForwardUser(Base):
    __tablename__ = 'dyn_forward_user'

    id: Mapped[Optional[int]] = mapped_column(Integer, primary_key=True, unique=True)
    uid: Mapped[Optional[int]] = mapped_column(Integer)
    uname: Mapped[Optional[int]] = mapped_column(Integer)


class DynLotteryList(Base):
    __tablename__ = 'dyn_lottery_list'

    id: Mapped[Optional[int]] = mapped_column(Integer, primary_key=True, unique=True)
    dyn_id: Mapped[Optional[int]] = mapped_column(Integer)
    up_id: Mapped[Optional[int]] = mapped_column(Integer)


class DynLotteryUp(Base):
    __tablename__ = 'dyn_lottery_up'

    id: Mapped[Optional[int]] = mapped_column(Integer, primary_key=True, unique=True)
    uid: Mapped[Optional[int]] = mapped_column(Integer)
    uname: Mapped[Optional[int]] = mapped_column(Integer)
    level: Mapped[Optional[int]] = mapped_column(Integer)
    avater: Mapped[Optional[int]] = mapped_column(Integer)
