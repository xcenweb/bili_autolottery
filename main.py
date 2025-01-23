import asyncio
from datetime import datetime

import config
import util.scheduler
import util.dynamics
from test_auto import auto_lottery

async def update_dynamics():
    """
    更新动态数据
    """
    print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"), '----开始抓取动态----')

    ids = config.get('lottery.ids')
    for uid in ids:
        await util.dynamics.get_repost_dynamic(uid)

    print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"), '----动态抓取结束----')


async def main():
    """
    主函数，设置定时任务
    """
    util.scheduler.start()

    # 添加定时任务，每6小时执行一次
    await util.scheduler.add_job(update_dynamics, 'update_dynamics', 'interval', hours=6)
    await util.scheduler.add_job(auto_lottery, 'auto_lottery', 'interval', hours=6, minutes=45)
    await util.scheduler.list_jobs()

    try:
        await asyncio.get_event_loop().create_future()
    except (KeyboardInterrupt, SystemExit):
        util.scheduler.stop()
        asyncio.get_event_loop().stop()

if __name__ == '__main__':
    asyncio.run(main())