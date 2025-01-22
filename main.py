import asyncio
from datetime import datetime

import config
import util.scheduler
import util.dynamics

async def get_new_dynamics():
    """
    获取转发号池中所有新动态，进行处理后存入数据库
    """
    print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"), '----开始获取新动态----')
    ids = config.get('lottery.ids')

    for id in ids:
        print(id)
        user_info, dynamic_list, has_more, next_offset, last_time = await util.dynamics.get_repost_dynamic(id)
        print(user_info)
        print(dynamic_list)
        print(has_more)
        print(next_offset)
        print(last_time)

        asyncio.sleep(10)

    print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"), '----获取新动态结束----')


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
    # 添加定时任务，每6小时执行一次
    await util.scheduler.add_job(get_new_dynamics, 'get_new_dynamics', 'interval', hours=6)
    await util.scheduler.add_job(auto_lottery, 'auto_lottery', 'interval', hours=6)

    try:
        # 保持程序运行
        await asyncio.get_event_loop().create_future()
    except (KeyboardInterrupt, SystemExit):
        util.scheduler.stop()
        asyncio.get_event_loop().stop()

if __name__ == '__main__':
    asyncio.run(main())