# 对抽奖转发号动态进行获取操作
import datetime
from timeit import repeat
import config
from util import login, database

import json
import time

from bilibili_api import user, dynamic, comment
from bilibili_api.user import RelationType
from bilibili_api.comment import CommentResourceType



async def get_repost_dynamic(uid, offset=0):
    """
    获取一次某个账号下的转发动态
    :param uid: 抽奖号id
    :param offset: 偏移量
    :return: user_info, dynamic_list, has_more, next_offset, last_time
    """
    usr = user.User(uid, login.get_credential())
    dyn_page = await usr.get_dynamics(offset)

    has_more = dyn_page['has_more'] # 是否还有更多
    next_offset = dyn_page['next_offset'] # 下一次的偏移量
    dynamic_cards = dyn_page['cards'] # 动态列表信息

    dynamic_list = []
    for item in dynamic_cards:

        desc = item.get('desc') # 动态描述
        card = item.get('card') # 动态内容

        if card.get('origin_user') is None or card.get('origin') is None:
            print('不是转发的动态，跳过')
            continue

        if card.get('item').get('miss') == 1:
            print('源动态被隐藏或删除，跳过')
            continue

        user_profile = desc.get('user_profile') # 转发动态用户信息
        origin_user = card.get('origin_user')   # 原动态用户信息
        origin = json.loads(card.get('origin')) # 原动态内容摘要

        dynamic_list.append({
            'repost': {
                'id': desc.get('dynamic_id'), # 动态id
                'content': desc.get('content'), # 转发时附言
                'timestamp': desc.get('timestamp'), # 转发时间
            },
            'origin': {
                'id': desc.get('orig_dy_id'), # 原动态id
                'content': origin.get('item').get('description') or origin.get('item').get('content'), # 原动态内容
                'user': {
                    'id': origin_user['info']['uid'], # 原动态up的uid
                    'name': origin_user['info']['uname'], # 原动态up的昵称
                    'avatar': origin_user['info']['face'], # 原动态up的头像
                    'level': origin_user['level_info']['current_level'], # 原动态up的等级
                },
            }
        })

    user_info = {
        'id': user_profile['info']['uid'], # 抽奖转发号id
        'name': user_profile['info']['uname'], # 抽奖转发号昵称
        'avatar': user_profile['info']['face'], # 抽奖转发号头像
        'level': user_profile['level_info']['current_level'], # 抽奖转发号等级
    }

    print(f'抓取转发动态数量：{len(dynamic_list)}，是否还有下一篇：{has_more}，下一篇动态id：{next_offset}, 最后一条动态时间：{last_time}')

    return user_info, dynamic_list, has_more, next_offset


async def get_user_dynamics(uid):
    """
    获取一个用户的 新动态/全部动态 处理后存储进数据库
    :param uid: 用户ID
    :return: 用户信息, 动态列表
    """
    dynamic_deep = config.get('dynamic.deep') # 最大天数
    this_ts = int(time.time() * 1000)
    offset = 0

    while True:
        user_info, dynamic_list, has_more, next_offset = await get_repost_dynamic(uid, offset)

        if not database.exist_user(uid):
            database.insert_user(
                uid=user_info['id'],
                name=user_info['name'],
                face=user_info['avatar'],
                level=user_info['level'],
            )

        for dyn in dynamic_list:
            dyn_id = dyn['origin']['id']
            repost_ts = dyn['repost']['timestamp']

            if this_ts - repost_ts > dynamic_deep * 24 * 60 * 60 * 1000:
                print(f'动态 {dyn_id} 超过最大天数，退出')
                has_more = 0
                break

            if database.exist_dynamic(dyn_id):
                print(f'动态 {dyn_id} 已存在，跳过')
                continue
            else:
                database.insert_dynamic(dyn)
                print(f'动态 {dyn_id} 插入成功')

        if has_more == 1:
            offset = next_offset
            asyncio.sleep(15)
            continue
        else:
            break

    return True



async def participate_lottery(dyn_id: int, up_id: int):
    """
    参加抽奖, 关注+点赞+评论+转发
    :param dyn_id: 抽奖动态id
    :param up_id: 抽奖up的id
    """
    dyn = dynamic.Dynamic(dyn_id, login.get_credential())
    usr = user.User(up_id, login.get_credential())

    try:
        await usr.modify_relation(RelationType.SUBSCRIBE)
    except Exception as e:
        pass

    time.sleep(1.5)
    await dyn.set_like(status=True)

    time.sleep(1.5)
    await comment.send_comment(text="测试1下", oid=dyn_id, type_=CommentResourceType.DYNAMIC, credential=login.get_credential())

    time.sleep(1.5)
    await dyn.repost(text="转发动态")

    return True