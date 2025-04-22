# 测试
# 用户： 关注、关注分组
# 动态： 转发、点赞、评论

from app.core.login import get_credential
from app.core.lottery import part
from bilibili_api import user, dynamic, comment
from bilibili_api.user import RelationType
from bilibili_api.comment import CommentResourceType

dynid = 1050702335255248900
uid = 178690106

async def test():
    # 是否关注
    usr = user.User(uid, get_credential())
    is_following = await usr.get_relation(178690106)
    print(is_following)

    # part(dynid, uid, ['comment'])

if __name__ == '__main__':
    import asyncio
    asyncio.run(test())