import asyncio
from datetime import datetime
import util.database
import util.dynamics

async def auto_lottery():
    """
    读取数据库，即时自动抽奖，apscheduler添加定时任务执行抽奖，抽奖后对数据库进行更新
    """
    print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"), '----开始设置自动抽奖任务----')

    # 连接数据库获取待分配任务的动态
    pending_dynamics = util.database.get_status_dynamic('pending')
    print(f'待分配任务动态数: {len(pending_dynamics)}')
    for dynamic in pending_dynamics:
        await util.dynamics.participate_lottery(dynamic.dynamic_id, dynamic.up_uid)
        print(f'成功参与抽奖 动态ID: {dynamic.dynamic_id}')
        util.database.update_status(dynamic.dynamic_id, 'participated')
        await asyncio.sleep(5)

    print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"), '----设置自动抽奖任务结束----')

if __name__ == '__main__':
    # 直接运行测试
    asyncio.run(auto_lottery())