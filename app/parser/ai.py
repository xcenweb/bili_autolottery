"""
对抽奖文章进行ai解析
"""

import json
from zhipuai import ZhipuAI
from datetime import datetime
import app.config as config

client = ZhipuAI(api_key=config.get('zhipuai.api_key'))

prompt = """
你需要判断是否是一篇抽奖动态、互动抽奖类型的文章，若不是只返回false，如果是则按照固定json格式返回相应信息，注意必须返回纯文本，不能有markdown

{"method":[],"gifts":[],"due_time":""}

method：抽奖类型
例如：转发抽奖、点赞抽奖、评论抽奖 "method":["repost","like","comment"]
如果没有说明就返回："method":["repost","like","comment"]

gifts：抽奖奖品
例如："gifts":[{"remark":"一等奖", "gift":"随机玩具"},{"remark":"二等奖", "gift":"随机零食"}]
也可能没有设定明确的奖项："gifts":[{"remark":"", "gift":"X870 EAGLE WIFI7"}]

due_time：抽奖截止时间
例如："2023-01-01 00:00:00"
如果没有就返回空字符串："due_time":""
如果不是标准 y-m-d h:m:s 格式，则对缺失部分进行补全，或返回"due_time":""
"""

def ai_parse(content: str) -> dict|bool:
    """
    通过 LLM 对普通抽奖内容进行解析处理
    :param content: 抽奖内容
    :return: 处理后的抽奖内容
    """
    response = client.chat.completions.create(
        model=config.get("zhipuai.model"),  # 填写需要调用的模型编码
        messages=[
            {"role": "system", "content": prompt},
            {"role": "user", "content": content}
        ]
    )
    response_text = response.choices[0].message.content.strip()
    try:
        if response_text.lower() == "false":
            return False

        data = json.loads(response_text)
        return {
            "method": data['method'] if not data['method'] else ["repost","like","comment"],
            "gifts": data['gifts'] if not data['gifts'] else [],
            "due_time": data['due_time'] if not data['due_time'] else datetime.fromisoformat(due_time).strftime("%Y-%m-%d %H:%M:%S")
        }
    except json.JSONDecodeError as e:
        print(f"JSON parsing error: {e}")
        return False