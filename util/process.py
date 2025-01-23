# 对抽奖文章进行解析处理

from zhipuai import ZhipuAI
import json

client = ZhipuAI(api_key="32c6da5d1ee49a35f49af6342e1daac6.SGBjVGhijpCYJFrb")

def ai_parse_content(content) -> dict:
    """
    通过 LLM 对普通抽奖内容进行解析处理
    :param content: 抽奖内容
    :return: 处理后的抽奖内容
    """
    prompt = open("./data/prompt.md", "r", encoding="utf-8").read()
    response = client.chat.completions.create(
        model="GLM-4-Flash",  # 填写需要调用的模型编码
        messages=[
            {"role": "system", "content": prompt},
            {"role": "user", "content": content}
        ]
    )

    response_text = response.choices[0].message.content.strip()
    try:
        # 如果返回的是 "false"，返回空字典
        if response_text.lower() == "false":
            return False
        return json.loads(response_text)
    except json.JSONDecodeError as e:
        print(f"JSON parsing error: {e}")
        return False


def web_parse_gifts(dyn_id) -> list:
    """
    通过无头浏览器爬取动态抽奖奖品信息
    """
    pass