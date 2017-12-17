import urllib.request
import zlib


def deflate(data):
    try:
        return zlib.decompress(data, -zlib.MAX_WBITS)
    except zlib.error:
        return zlib.decompress(data)


def danmu_download(id):
    url = 'https://comment.bilibili.com/%s.xml' % id
    try:
        with urllib.request.urlopen(url) as f:
            danmu = f.read()
    except Exception as e:
        print(e)
        return None
    try:
        danmu_deflate = deflate(danmu)
    except Exception as e:
        print(e)
        return None
    return danmu_deflate
