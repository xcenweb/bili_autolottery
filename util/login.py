# 处理登录

import os
import json
import config

from bilibili_api import login, user, sync
from bilibili_api.login import Credential


login_cacheFile = os.getcwd() + config.get('login.cache')


def get_cache() -> Credential:
    """
    获取credential缓存
    """
    # 如果存在缓存，则直接读取
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
    # 若不存在缓存或登录失效，则重新登录
    if not os.path.exists(login_cacheFile) or get_cache() is None:
        if config.get('login.type') == 'qrcode':
            credential = qrcode_login()
        else:
            raise Exception('登录方式不受支持')
        set_cache(credential)
        return credential
    else:
        return get_cache()


### 登录方式 ###

def qrcode_login() -> Credential:
    """
    使用二维码登录
    """
    credential = login.login_with_qrcode()

    try:
        credential.raise_for_no_bili_jct()
        credential.raise_for_no_sessdata()
    except Exception as e:
        raise Exception('扫码登录失败')

    return credential