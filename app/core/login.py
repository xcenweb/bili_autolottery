"""
登录
"""

import os
import json
import app.config as config

from bilibili_api import login
from bilibili_api.login import Credential

login_type = config.get('login.type')
login_cacheFile = os.getcwd() + config.get('login.cache')

def get_cache() -> Credential:
    """
    获取credential缓存
    """
    try:
        d = json.load(open(login_cacheFile, mode='r'))
        if d == {}:
            return None
        return Credential(
            sessdata=d['SESSDATA'],
            bili_jct=d['bili_jct'],
            buvid3=d['buvid3'],
            dedeuserid=d['DedeUserID'],
            ac_time_value=d['ac_time_value']
        )
    except:
        return None


def set_cache(credential: Credential):
    """
    设置credential缓存
    """
    data = credential.get_cookies()
    json.dump(data, open(login_cacheFile, mode='w'))


def get_credential() -> Credential:
    """
    获取登录凭证
    """
    if not os.path.exists(login_cacheFile) or get_cache() is None:
        if login_type == 'qrcode':
            credential = qrcode_login()
        else:
            print('请先配置正确的登录方式')
            return None
        if credential is None:
            print('登录失败')
            return None
        set_cache(credential)
        return credential
    else:
        return get_cache()


def qrcode_login() -> Credential:
    """
    使用二维码登录
    """
    credential = login.login_with_qrcode()
    try:
        credential.raise_for_no_bili_jct()
        credential.raise_for_no_sessdata()
    except Exception as e:
        return None
    return credential