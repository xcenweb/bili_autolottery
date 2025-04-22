"""
数据库配置和连接管理 (异步版本)
"""

import asyncio
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy import text
from sqlalchemy.orm import DeclarativeBase
import app.config as config
from contextlib import asynccontextmanager

# 创建异步数据库引擎
engine = create_async_engine(
    config.get('db.url'),
    pool_pre_ping=True,
    pool_recycle=3600,
    echo=False,
)

# 创建异步会话工厂
AsyncSessionLocal = async_sessionmaker(
    engine,
    class_=AsyncSession,
    expire_on_commit=False,
    autocommit=False,
    autoflush=False,
)

@asynccontextmanager
async def get_db():
    """
    获取数据库会话 (异步)
    """
    async with AsyncSessionLocal() as session:
        yield session
async def test_get_db_session():
    """
    测试获取数据库会话 (异步)
    """
    async with get_db() as db:
        # 异步执行 SQL
        res = await db.execute(text("show tables"))
        print(res.fetchall())

async def main():
    await test_get_db_session()
    await engine.dispose()

if __name__ == "__main__":
    asyncio.run(main())
