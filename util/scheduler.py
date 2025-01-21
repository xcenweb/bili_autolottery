from apscheduler.schedulers.background import BackgroundScheduler

scheduler = BackgroundScheduler()
scheduler.start()

def add_job(task_name, jobfunc, trigger, **kwargs):
    """
    添加一个新的定时任务。

    :param task_name: 任务名称，用于标识任务
    :param trigger: 触发器类型，例如 "interval" 或 "cron"
    :param kwargs: 触发器的额外参数（例如 seconds, minutes 等）
    :return: 添加的任务对象
    """
    job = scheduler.add_job(jobfunc, trigger, args=[task_name], **kwargs)
    print(f"任务 {task_name} 已添加，Job ID: {job.id}")
    return job

def remove_job_by_name(task_name):
    """
    根据任务名称删除任务。

    :param task_name: 任务名称，用于查找和删除任务
    """
    jobs = scheduler.get_jobs()
    for job in jobs:
        if job.args[0] == task_name:  # 通过任务名称进行匹配
            job.remove()
            print(f"任务 {task_name} 已删除")
            return
    print(f"任务 {task_name} 不存在")

def list_jobs():
    """
    列出当前所有任务。

    打印每个任务的 ID、名称以及触发器信息。
    """
    jobs = scheduler.get_jobs()
    if not jobs:
        print("没有任务在运行")
    for job in jobs:
        print(f"任务 ID: {job.id}, 任务名称: {job.args[0]}, 触发器: {job.trigger}")

def modify_job_by_name(task_name, trigger, **kwargs):
    """
    修改指定任务的触发器。

    :param task_name: 任务名称，用于查找任务
    :param trigger: 新的触发器类型，例如 "interval" 或 "cron"
    :param kwargs: 新触发器的参数（例如 seconds, minutes 等）
    """
    jobs = scheduler.get_jobs()
    for job in jobs:
        if job.args[0] == task_name:  # 通过任务名称进行匹配
            # 使用 reschedule() 更新任务的触发器
            job.reschedule(trigger, **kwargs)
            print(f"任务 {task_name} 的触发器已修改为 {trigger} {kwargs}")
            return
    print(f"任务 {task_name} 不存在")