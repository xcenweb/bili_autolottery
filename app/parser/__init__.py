"""
动态解析器
"""

from .ai import ai_parse
from .web import web_parse

def dyn_parser(dyn_id: int, content: str):
    """
    动态通用解析器
    :param dyn_id: 动态id
    :param content: 动态内容
    :return: 数据
    """

    ai_result = ai_parse(dyn_content['origin']['content'])
    if ai_result:
        # ai获取到了信息，尝试解析
        print('ai解析成功')

        type = ai_result['type'] if ai_result['type'] else ["common"]
        gifts = ai_result['gifts'] if ai_result['gifts'] else []
        due_time = ai_result['due_time'] if ai_result['due_time'] else datetime.fromisoformat(due_time).strftime("%Y-%m-%d %H:%M:%S")

    # ai获取不全信息，从浏览器直接抓取
    print('ai获取不全信息，从网页直接抓取')

    data = web_parse(dyn_id)
    type = data['type']
    gifts = data['gifts']
    due_time = data['due_time']
    auto_time = datetime.fromisoformat(due_time).strftime("%Y-%m-%d %H:%M:%S") - advance_seconds

    return type, gifts, due_time, auto_time