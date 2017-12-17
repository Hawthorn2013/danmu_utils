import urllib.request


class danmu_diyidan_download(object):
    def danmu_download(self, id):
        url = 'https://www.diyidan.com/main/post/danmu?postId=%s' % id
        try:
            with urllib.request.urlopen(url) as f:
                danmu = f.read()
        except Exception as e:
            print(e)
            return None
        return danmu
