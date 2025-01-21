import config
import util.dynamics
import time
import asyncio

from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.schedulers.background import BackgroundScheduler

"""
1：每天4:00定时获取转发号池中所有新动态，进行处理后存入数据库
2：读取数据库，执行 定时/即时 自动抽奖，抽奖后对数据库进行更新
"""

async def get_new_dynamics():
    """
    获取转发号池中所有新动态，进行处理后存入数据库
    """
    print(time.ctime(time.time()), '开始获取新动态')
    await asyncio.sleep(2)
    print(time.ctime(time.time()), '获取新动态结束，存储结束')

async def auto_lottery():
    """
    读取数据库，即时自动抽奖，apscheduler添加定时任务执行抽奖，抽奖后对数据库进行更新
    """
    print(time.ctime(time.time()), '开始自动抽奖')
    await asyncio.sleep(2)
    print(time.ctime(time.time()), '自动抽奖结束，更新数据库结束')

if __name__ == '__main__':
    scheduler = BackgroundScheduler()
    scheduler.add_job(func=get_new_dynamics, trigger='cron', hour=4, minute=0)
    scheduler.start()
    try:
        asyncio.get_event_loop().run_forever()
    except (KeyboardInterrupt, SystemExit):
        pass