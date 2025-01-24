from playwright.sync_api import sync_playwright, TimeoutError as PlaywrightTimeoutError
from datetime import datetime

def parse_lottery_end_time(end_time_str: str) -> str:
    try:
        # 将中文日期字符串转换为标准日期格式
        end_time_str = end_time_str.replace('年', '-').replace('月', '-').replace('日', '').replace(' ', ' ')
        end_time = datetime.strptime(end_time_str, '%Y-%m-%d %H:%M')
        return end_time.strftime('%Y-%m-%d %H:%M:%S')
    except ValueError as e:
        print(f"日期解析错误: {e}")
        return None

def parse_lottery_condition(condition_text: str) -> list:
    """
    解析抽奖条件，将文字转化为操作列表。
    """
    conditions = []
    condition_text = condition_text.lower()

    if '关注' in condition_text or 'follow' in condition_text:
        conditions.append("follow")
    if '评论' in condition_text or 'comment' in condition_text:
        conditions.append("comment")
    if '点赞' in condition_text or 'like' in condition_text:
        conditions.append("like")
    if '转发' in condition_text or 'repost' in condition_text:
        conditions.append("repost")

    return conditions

def get_lottery_details(business_id: str):
    url = f"https://www.bilibili.com/h5/lottery/result?business_type=1&business_id={business_id}&isWeb=1"

    try:
        with sync_playwright() as p:
            # 启动浏览器
            browser = p.chromium.launch(headless=True)
            page = browser.new_page()

            try:
                # 跳转到目标页面
                page.goto(url, timeout=10000)  # 10秒超时
                # 等待页面加载完成，可以调整等待的元素选择器
                page.wait_for_selector("#app > div > div > div.lottery-result__content > div > div.lottery__section.line.desc > div:nth-child(1) > div.lottery__desc__value", timeout=10000)

                # 获取抽奖结束时间
                end_time_element = page.query_selector("#app > div > div > div.lottery-result__content > div > div.lottery__section.line.desc > div:nth-child(1) > div.lottery__desc__value")
                if end_time_element:
                    end_time_text = end_time_element.inner_text().strip()
                    formatted_end_time = parse_lottery_end_time(end_time_text)
                else:
                    print("未找到抽奖结束时间元素")
                    formatted_end_time = None

                # 获取抽奖条件
                condition_element = page.query_selector("#app > div > div > div.lottery-result__content > div > div.lottery__section.line.desc > div:nth-child(2) > div.lottery__desc__value")
                if condition_element:
                    lottery_condition_text = condition_element.inner_text().strip()
                    lottery_condition = parse_lottery_condition(lottery_condition_text)
                else:
                    print("未找到抽奖条件元素")
                    lottery_condition = None

                # 获取奖品列表
                prize_list_element = page.query_selector(".prizes__list")
                prize_list = []
                if prize_list_element:
                    prize_elements = prize_list_element.query_selector_all(".prize")
                    for prize_element in prize_elements:
                        prize_level = prize_element.query_selector(".prize__level").inner_text().strip()
                        prize_desc = prize_element.query_selector(".prize__desc").inner_text().strip()

                        prize_list.append({
                            "remark": prize_level,  # 奖品等级
                            "gift": prize_desc      # 奖品描述
                        })
                else:
                    print("未找到奖品列表元素")

                # 关闭浏览器
                browser.close()

                # 返回指定格式的结果
                return {
                    "type": lottery_condition or [],
                    "gifts": prize_list,
                    "due_time": formatted_end_time or ""
                }

            except PlaywrightTimeoutError as e:
                print(f"页面加载或元素定位超时: {e}")
                browser.close()
                return None
            except Exception as e:
                print(f"页面处理过程中发生错误: {e}")
                browser.close()
                return None

    except Exception as e:
        print(f"浏览器启动或初始化错误: {e}")
        return None

# 示例调用函数，传入业务ID
business_id = "1012603175036780583"  # 替换为你的业务ID
lottery_details = get_lottery_details(business_id)

if lottery_details:
    print(lottery_details)
else:
    print("未能获取抽奖详情")
