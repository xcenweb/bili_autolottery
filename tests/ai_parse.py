# 测试ai解析

from app.parser.ai import ai_parse

dyn_content = """
​互动抽奖感谢各位新粉老粉的支持，本次准备了4份好物，总价值10396元。 关注@搞机所 转发此动态即可参与官方工具互动抽奖，礼物清单如下:

一等奖：华为 Mate 70 Pro 雪域白 12GB+512GB 抽一位 价值6499元
二等奖：华硕TUF GAMING Z790-PLUS WIFI D5 抽一位 价值2199元
三等奖：雷克沙内存DDR5 6800 C34 32GB(16GB*2) 雷神显示器 CF25F300L 各抽一位 共2人 总价值1698元

最后搞机所电脑，电脑主机热卖中，需要的小伙伴可以去店铺看看哦！店铺链接：​搞机所 办公电竞主播台式...
"""

ai_result = ai_parse(dyn_content)
print(ai_result)