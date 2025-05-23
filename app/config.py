"""
项目配置
"""

import toml

__VERSION__ = '0.0.1'
# sqlacodegen --outfile model.py sqlite:///./data/dyn_lottery.db

settings = toml.load('./data/setting.toml')
def get(key: str, default=None):
    """
    点式路径获取配置
    :param key: 点式路径
    :return: 配置值
    """
    keys = key.split('.')
    try:
        if len(keys) == 1:
            return settings.get(key, default)
        else:
            return settings.get(keys[0]).get(keys[1], default)
    except Exception as e:
        print(e)
        return default