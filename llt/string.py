# -*- coding: utf-8 -*-
import types


def unicode_truncate(uni, length, encoding='utf-8', dot=True):
    """
    按字节长度对字符串进行截取
    :param uni: 待截取字符串，unicode编码格式
    :param length: 截取后字符串长度
    :param encoding: 转换时采用的编码格式
    :param dot: 截取后末尾是否包含"..."
    :return: 截取后的字符串，unicode编码格式
    """
    encoded = uni.encode(encoding)
    if len(encoded) <= length:
        return uni

    triple_dot = '...' if dot else ''
    return u'%s%s' % (encoded[:length - len(triple_dot)].decode(encoding, 'ignore'), triple_dot)


def smart_str(s, encoding='utf-8', strings_only=False, errors='strict'):
    """
    Returns a bytestring version of 's', encoded as specified in 'encoding'.
    If strings_only is True, don't convert (some) non-string-like objects.
    """
    if strings_only and isinstance(s, (types.NoneType, int)):
        return s
    if not isinstance(s, basestring):
        try:
            return str(s)
        except UnicodeEncodeError:
            if isinstance(s, Exception):
                # An Exception subclass containing non-ASCII data that doesn't
                # know how to print itself properly. We shouldn't raise a
                # further exception.
                return ' '.join([smart_str(arg, encoding, strings_only,
                                           errors) for arg in s])
            return unicode(s).encode(encoding, errors)
    elif isinstance(s, unicode):
        return s.encode(encoding, errors)
    elif s and encoding != 'utf-8':
        return s.decode('utf-8', errors).encode(encoding, errors)
    else:
        return s

