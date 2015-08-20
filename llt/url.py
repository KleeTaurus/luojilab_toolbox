# -*- coding: utf-8 -*-
import hashlib
from .utils import smart_str


def format_url(params):
    """
    将字典对象转换为url字符串（采用utf8编码），如果key对象的value为空，转换后的字符串中将忽略该key值。
    :param params: 字典对象
    :return: url字符串
    """
    return '&'.join(['%s=%s' % (smart_str(k), smart_str(params[k])) for k in sorted(params) if params[k]])


def encode_dict(params):
    """
    将字典对象中的value值转换为utf8编码，去除value值为空的健值对。
    :param params: 字典对象
    :return: utf8编码格式的字典对象
    """
    return {k: smart_str(params[k]) for k in params if params[k]}


def sign_url(params, key_secret, key_name=None, sign_type='md5', upper_case=False):
    """
    计算url参数签名
    :param params: 待签名字典对象
    :param key_secret: 签名密钥
    :param key_name: 签名名称
    :param sign_type: 签名方式 md5/sha1
    :param upper_case: 是否将签名转换为大写字母
    :return: 签名值
    """
    url = format_url(params)
    url = '%s&%s=%s' % (url, key_name, key_secret) if key_name else '%s%s' % (url, key_secret)

    if sign_type == 'md5':
        digest = hashlib.md5(url).hexdigest()
    elif sign_type == 'sha1':
        digest = hashlib.sha1(url).hexdigest()
    else:
        raise NotImplementedError('Method %s is not supported' % sign_type)

    return digest.upper() if upper_case else digest
