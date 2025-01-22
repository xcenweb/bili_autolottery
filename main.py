import asyncio
from datetime import datetime

import config
import util.scheduler
import util.dynamics

async def update_dynamics():
    """
    更新数据库中存储的抽奖动态
    """
    print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"), '----开始抓取动态----')

    ids = config.get('lottery.ids')
    for uid in ids:
        await util.dynamics.get_user_new_dynamics(uid)

    print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"), '----动态抓取结束----')

async def auto_lottery():
    """
    读取数据库，即时自动抽奖，apscheduler添加定时任务执行抽奖，抽奖后对数据库进行更新
    """
    print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"), '开始自动抽奖')
    await asyncio.sleep(2)
    print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"), '自动抽奖结束，更新数据库结束')


async def main():
    """
    主函数，设置定时任务
    """
    await update_dynamics()

    # 添加定时任务，每6小时执行一次
    await util.scheduler.add_job(update_dynamics, 'update_dynamics', 'interval', hours=6)
    await util.scheduler.add_job(auto_lottery, 'auto_lottery', 'interval', hours=6)

    try:
        # 保持程序运行
        await asyncio.get_event_loop().create_future()
    except (KeyboardInterrupt, SystemExit):
        util.scheduler.stop()
        asyncio.get_event_loop().stop()


if __name__ == '__main__':
    asyncio.run(main())