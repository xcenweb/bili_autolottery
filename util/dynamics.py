# 对抽奖号动态进行获取操作
import config
from util import login

import json
import time
import time

from bilibili_api import user, sync, dynamic, comment
from bilibili_api.user import RelationType
from bilibili_api.comment import CommentResourceType

ids = config.get('lottery.ids') # 抽奖号id池

async def get_repost_dynamic(uid, offset=0):
    """
    获取一次某个账号下的转发动态
    :param uid: 抽奖号id
    :param offset: 偏移量
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
        # extend_json = item['extend_json'] # 动态扩展信息
        # display = item['display'] # 动态展示信息

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
                'id': desc.get('dynamic_id'), # 转发动态id
                'content': desc.get('content'), # 转发时附言
                'time': time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(desc.get('timestamp'))), # 转发时间
            },
            'origin': {
                'id': desc.get('orig_dy_id'), # 原动态id
                'content': origin.get('item').get('description') or origin.get('item').get('content'), # 原动态内容
                'user': {
                    'id': origin_user['info']['uid'], # 原动态up的id
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
    last_time = dynamic_list[-1]['repost']['time']

    # print(dynamic_list)
    print(f'转发动态数量：{len(dynamic_list)}，是否还有下一篇：{has_more}，下一篇动态id：{next_offset}, 最后一条动态时间：{last_time}')

    return user_info, dynamic_list, has_more, next_offset, last_time


async def get_lottery_dynamic(dynamic_list: list):
    """
    TODO 整理抽奖动态列表
        - dyn_id 抽奖动态id
        - type 抽奖类型：视频评论抽奖(video)、官方抽奖工具抽奖(official)、第三方抽奖工具抽奖(third)、普通抽奖(normal)
        - content 抽奖动态内容
        - gifts 抽奖奖品清单
        - due_time 抽奖截止时间
    :param dynamic_list: 抽奖动态列表
    :return: 抽奖动态列表
    """
    lottery_dynamic = []

    for item in dynamic_list:
        originId = item.get('origin').get('id')
        dyn = dynamic.Dynamic(originId, login.get_credential())
        info = sync(dyn.get_info())
        lottery_dynamic.append({
            'dyn_id': originId,
            'type': '',
            'content': '',
            'gifts': '',
            'manner': '',
            'due_time': '',
        })
    return lottery_dynamic


async def participate_lottery(dyn_id: int, up_id: int):
    """
    参加抽奖, 关注+点赞+评论+转发
    :param dynamic_list: 抽奖动态列表
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