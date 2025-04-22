"""
抽奖操作
"""

from bilibili_api.login import login

async def part(dyn_id: int, up_id: int, method: [str]):
    """
    参加抽奖
    :param dyn_id: 抽奖动态id
    :param up_id: 抽奖up的id
    :param method: 参与方式
    :return:
    """
    dyn = dynamic.Dynamic(dyn_id, login.get_credential())
    usr = user.User(up_id, login.get_credential())

    try:
        await usr.modify_relation(RelationType.SUBSCRIBE)
    except Exception as e:
        pass

    if 'like' in method:
        # 动态点赞
        await dyn.set_like(status=True)
    if 'comment' in method:
        # 动态评论
        await comment.send_comment(text="测试1下", oid=dyn_id, type_=CommentResourceType.DYNAMIC, credential=login.get_credential())
    if 'repost' in method:
        # 动态转发
        await dyn.repost(text="转发动态")
    if 'follow' in method:
        # 关注up
        await usr.modify_relation(RelationType.FOLLOW)

    return True