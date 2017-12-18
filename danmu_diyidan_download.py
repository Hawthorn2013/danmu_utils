import urllib.request


class danmu_diyidan_download(object):
    def __init__(self, param):
        if param != 'videoId' and param != 'postID':
            raise Exception('Invalid param: "%s".' % param)
        self.param = param

    def danmu_download(self, id):
        url = 'https://api.diyidan.net/v0.2/posts/danmaku?%s=%s' % (self.param, id)
        try:
            with urllib.request.urlopen(url) as f:
                danmu = f.read()
        except Exception as e:
            print(e)
            return None
        return danmu
