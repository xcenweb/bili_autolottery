# 项目配置

import toml

__VERSION__ = '0.0.2'
__DB__ = 'sqlite:///./data/dyn_lottery.db' # sqlacodegen --outfile model.py sqlite:///./data/dyn_lottery.db

settings = toml.load('./data/setting.toml')
def get(key: str):
    """
    根据点式路径获取配置
    :param key: 点式路径
    :return: 配置值
    """
    keys = key.split('.')
    try:
        if len(keys) == 1:
            return settings.get(key)
        else:
            return settings.get(keys[0]).get(keys[1])
    except Exception as e:
        print(e)
        return None