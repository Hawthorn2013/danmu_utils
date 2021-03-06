import urllib.request
import time

class danmu_diyidan_download(object):
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
    def danmu_download_file(line, ts=False):
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
        timestamp = time.strftime('%Y%m%d%H%M%S', time.localtime())
        res = danmu_diyidan_download.danmu_download(videoId=videoId, postId=postId)
        if 'videoId' in res:
            out_filename = ''
            if postId != None:
                out_filename = out_filename + postId
            out_filename = out_filename + '-' + videoId
            if ts:
                out_filename = out_filename + '_' + timestamp
            out_filename = out_filename + '.' + 'dydjson'
            try:
                with open(out_filename, mode='wb') as f:
                    f.write(res['videoId'])
                print('Success generate file: "%s".' % out_filename)
            except Exception as e:
                print(e)
        if 'postId' in res:
            out_filename = postId + '-'
            if ts:
                out_filename = out_filename + '_' + timestamp
            out_filename = out_filename + '.' + 'dydjson'
            try:
                with open(out_filename, mode='wb') as f:
                    f.write(res['postId'])
                print('Success generate file: "%s".' % out_filename)
            except Exception as e:
                print(e)
