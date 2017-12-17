import urllib.request


def danmu_download(id):
    url = 'https://www.diyidan.com/main/post/danmu?postId=%s' % id
    try:
        with urllib.request.urlopen(url) as f:
            danmu = f.read()
    except Exception as e:
        print(e)
        return None
    return danmu
