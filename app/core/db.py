"""
数据库配置和连接管理
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
    获取数据库会话
    """
    async with AsyncSessionLocal() as session:
        try:
            yield session
        finally:
            await session.close()