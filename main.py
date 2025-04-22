import asyncio
from datetime import datetime

import config

import app.core.dynamics as dynamics
import app.utils.scheduler as scheduler

async def update_dynamics():
    """
    更新和爬取动态数据
    """
    print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"), '----开始抓取动态----')

    ids = config.get('lottery.ids')
    for uid in ids:
        await dynamics.get_repost_dynamic(uid)

    print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"), '----动态抓取结束----')


async def main():
    """
    主函数，设置定时任务
    """
    util.scheduler.start()

    # 定时任务
    await util.scheduler.add_job(update_dynamics, 'update_dynamics', 'interval', hours=6) # 每6小时执行一次爬取动态

    # 当前定时任务列表
    await util.scheduler.list_jobs()

    try:
        await asyncio.get_event_loop().create_future()
    except (KeyboardInterrupt, SystemExit):
        util.scheduler.stop()
        asyncio.get_event_loop().stop()


if __name__ == '__main__':
    asyncio.run(main())