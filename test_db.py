import config

from sqlalchemy import create_engine
from database import LotteryDynamics, RepostUsers, UpUsers

# 创建数据库引擎
engine = create_engine(config.__DB__)

# 读取数据库
with engine.connect() as conn:
    print(conn.execute(LotteryDynamics.__table__.select()).all())
    print(conn.execute(RepostUsers.__table__.select()).all())
    print(conn.execute(UpUsers.__table__.select()).all())