from apscheduler.schedulers.asyncio import AsyncIOScheduler
from datetime import datetime

scheduler = AsyncIOScheduler()
scheduler.start()

# 打印日志函数
def log_message(message, task_name=None):
    """
    打印日志信息，统一格式。

    :param message: 日志内容
    :param task_name: 可选，任务名称，用于标识任务相关日志
    """
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    task_info = f"[{task_name}] " if task_name else ""
    print(f"[apscheduler] {timestamp} {task_info}{message}")

async def add_job(func, task_name, trigger, **kwargs):
    """
    添加一个新的定时任务。

    :param func: 要执行的函数
    :param task_name: 任务名称，用于标识任务
    :param trigger: 触发器类型，例如 "interval" 或 "cron"
    :param kwargs: 触发器的参数（例如 seconds, minutes 等）
    """
    job = scheduler.add_job(func=func, trigger=trigger, name=task_name, **kwargs)
    log_message(f"任务已添加，Job ID: {job.id}", task_name)
    return job

async def remove_job_by_name(task_name):
    """
    根据任务名称删除任务。

    :param task_name: 任务名称，用于查找和删除任务
    """
    jobs = scheduler.get_jobs()
    found = False
    for job in jobs:
        if job.args[0] == task_name:  # 通过任务名称进行匹配
            job.remove()
            log_message("任务已删除", task_name)
            found = True
            break
    if not found:
        log_message("任务不存在", task_name)

async def list_jobs():
    """
    列出当前所有任务。

    打印每个任务的 ID、名称以及触发器信息。
    """
    jobs = scheduler.get_jobs()
    if not jobs:
        log_message("没有任务在运行")
    for job in jobs:
        log_message(f"任务 ID: {job.id}, 任务名称: {job.args[0]}, 触发器: {job.trigger}", job.args[0])

async def modify_job_by_name(task_name, trigger, **kwargs):
    """
    修改指定任务的触发器。

    :param task_name: 任务名称，用于查找任务
    :param trigger: 新的触发器类型，例如 "interval" 或 "cron"
    :param kwargs: 新触发器的参数（例如 seconds, minutes 等）
    """
    jobs = scheduler.get_jobs()
    found = False
    for job in jobs:
        if job.args[0] == task_name:  # 通过任务名称进行匹配
            # 使用 reschedule() 更新任务的触发器
            job.reschedule(trigger, **kwargs)
            log_message(f"任务的触发器已修改为 {trigger} {kwargs}", task_name)
            found = True
            break
    if not found:
        log_message("任务不存在", task_name)

def stop():
    scheduler.shutdown()


# 添加任务
# await util.scheduler.add_job("task_1", "interval", seconds=5)  # 每5秒执行一次
# await util.scheduler.add_job("task_2", "interval", seconds=10)  # 每10秒执行一次

# # 列出所有任务
# await util.scheduler.list_jobs()

# # 修改任务1的触发器，改为每3秒执行一次
# await asyncio.sleep(6)  # 等待任务1执行一轮
# await util.scheduler.modify_job_by_name("task_1", "interval", seconds=3)

# # 删除任务
# await asyncio.sleep(6)  # 等待任务1执行一轮
# await util.scheduler.remove_job_by_name("task_2")

# # 列出所有任务
# await util.scheduler.list_jobs()