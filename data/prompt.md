你需要判断是否是一篇抽奖动态、互动抽奖类型的文章，若不是只返回false，如果是则按照固定json格式返回相应信息，注意你需要返回txt纯文本，不能有md语法

{"type":[],"gifts":[],"due_time":""}

type：抽奖类型
例如：转发抽奖、点赞抽奖、评论抽奖 type=["repost","like","comment"]
如果没有说明就返回：["common"]

gifts：抽奖奖品
例如：[{"remark":"一等奖", "gift":"随机玩具"},{"remark":"二等奖", "gift":"随机零食"}]
也可能没有设定明确的奖项：[{"remark":"", "gift":"X870 EAGLE WIFI7"}]

due_time：抽奖截止时间
例如："2023-01-01 00:00:00"
如果没有就返回空字符串：""
如果不是标准 y-m-d h:m:s 格式，则对缺失部分进行补全或返回false