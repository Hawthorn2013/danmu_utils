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

    @staticmethod
    def danmu_download(videoId=None, postId=None):
        res = {}
        if videoId != None:
            url = 'https://api.diyidan.net/v0.2/posts/danmaku?videoId=%s' % (videoId)
            try:
                with urllib.request.urlopen(url) as f:
                    danmu = f.read()
                    res['videoId'] = danmu
            except Exception as e:
                print(e)
        if postId != None:
            url = 'https://api.diyidan.net/v0.2/posts/danmaku?postId=%s' % (postId)
            try:
                with urllib.request.urlopen(url) as f:
                    danmu = f.read()
                    res['postId'] = danmu
            except Exception as e:
                print(e)
        return res

    @staticmethod
    def danmu_download_file(line):
        line_params = line.strip('\n').split('\t')
        print('Start process item: "%s".' % line.strip('\n'))
        if len(line_params) < 2:
            return False
        if not line_params[0].isdecimal():
            return False
        if not line_params[1].isdecimal():
            return False
        videoId = line_params[0]
        postId = line_params[1]
        res = danmu_diyidan_download.danmu_download(videoId, postId)
        if 'videoId' in res:
            if postId != None:
                out_filename = '%s-%s.%s' % (postId, videoId, 'dydjson')
            else:
                out_filename = '-%s.%s' % (videoId, 'dydjson')
            try:
                with open(out_filename, mode='wb') as f:
                    f.write(res['videoId'])
                print('Success generate file: "%s".' % out_filename)
            except Exception as e:
                print(e)
        if 'postId' in res:
            out_filename = '%s-.%s' % (postId, 'dydjson')
            try:
                with open(out_filename, mode='wb') as f:
                    f.write(res['postId'])
                print('Success generate file: "%s".' % out_filename)
            except Exception as e:
                print(e)
