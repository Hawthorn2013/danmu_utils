import urllib.request
import zlib


class danmu_bilibili_download(object):
    @staticmethod
    def deflate(data):
        try:
            return zlib.decompress(data, -zlib.MAX_WBITS)
        except zlib.error:
            return zlib.decompress(data)

    @staticmethod
    def danmu_download(aid=None):
        res = {}
        if aid != None:
            url = 'https://comment.bilibili.com/%s.xml' % (aid)
            try:
                with urllib.request.urlopen(url) as f:
                    danmu = f.read()
                try:
                    danmu_deflate = danmu_bilibili_download.deflate(danmu)
                    res['aid'] = danmu_deflate
                except Exception as e:
                    print(e)
            except Exception as e:
                print(e)
        return res

    @staticmethod
    def danmu_download_file(line):
        line_params = line.strip('\n').split('\t')
        print('Start process item: "%s".' % line.strip('\n'))
        if len(line_params) < 1:
            return False
        if not line_params[0].isdecimal():
            return False
        aid = line_params[0]
        res = danmu_bilibili_download.danmu_download(aid=aid)
        if 'aid' in res:
            out_filename = '%s.%s' % (aid, 'xml')
            try:
                with open(out_filename, mode='wb') as f:
                    f.write(res['aid'])
                print('Success generate file: "%s".' % out_filename)
            except Exception as e:
                print(e)
