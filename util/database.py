import stat
import config
from datetime import datetime
from sqlalchemy import create_engine
from model import LotteryDynamics, RepostUsers, UpUsers

db = create_engine(config.__DB__)

def exist_dynamic(dyn_id):
    """
    判断动态是否存在
    """
    with db.connect() as conn:
        dyn = conn.execute(LotteryDynamics.__table__.select().where(LotteryDynamics.dynamic_id == dyn_id)).all()
        return dyn

def exist_up(up_id):
    """
    判断up是否有记录
    """
    with db.connect() as conn:
        up = conn.execute(UpUsers.__table__.select().where(UpUsers.uid == up_id)).all()
        return up

def exist_user(uid):
    """
    判断用户是否有记录
    """
    with db.connect() as conn:
        user = conn.execute(RepostUsers.__table__.select().where(RepostUsers.uid == uid)).all()
        return user

def insert_dynamic(dynamic_id, up_uid, type, content, gift_list, public_time, due_time, status):
    """
    增加一条动态
    """
    with db.connect() as conn:
        conn.execute(LotteryDynamics.__table__.insert().values(
            dynamic_id=dynamic_id, up_uid=up_uid, type=type, content=content, gift_list=gift_list,
            public_time=public_time, due_time=due_time, status=status, create_time=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        ))
        return conn.commit()

def insert_up(uid, name, face, level):
    """
    增加一条up信息
    """
    with db.connect() as conn:
        conn.execute(UpUsers.__table__.insert().values(
            uid=uid, name=name, face=face, level=level, create_time=datetime.now().strftime("%Y-%m-%d %H:%M:%S"), update_time=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        ))
        return conn.commit()

def insert_user(uid, name, face, level):
    """
    增加一条用户信息
    """
    with db.connect() as conn:
        conn.execute(RepostUsers.__table__.insert().values(
            uid=uid, name=name, face=face, level=level, create_time=datetime.now().strftime("%Y-%m-%d %H:%M:%S"), update_time=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        ))
        return conn.commit()

def update_status(dynamic_id, status):
    """
    更新动态状态
    """
    with db.connect() as conn:
        conn.execute(
            LotteryDynamics.__table__.update()
            .where(LotteryDynamics.dynamic_id == dynamic_id)
            .values(status=status)
        )
        conn.commit()

def get_status_dynamic(status):
    """
    获取指定状态的动态列表
    """
    with db.connect() as conn:
        dyn = conn.execute(LotteryDynamics.__table__.select().where(LotteryDynamics.status == status)).all()
        return dyn