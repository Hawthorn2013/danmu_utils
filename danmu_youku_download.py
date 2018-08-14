import urllib.request
import time
import urllib
from urllib.parse import urlencode
import json
import re

class danmu_diyidan_download(object):
    @staticmethod
    def danmu_download(videoId):
        res = {}
        param_now = {
            "mcount": "1",
            "ct": "1001",
            "iid": "920968192",
            "aid": "316739",
            "cid": "97",
            "lid": "0",
            "ouid": "0",
            # "_": "1531837670797",
        }
        danmu_collect = {
            "count": 0,
            "filtered": 1,
            "result": [],
        }
        param_now["iid"] = videoId
        j = 0
        while(True):
            param_now["mat"] = j
            query = urlencode(param_now)
            url = "https://service.danmu.youku.com/list?%s" % query
            print('Start download: "%s".' % url)
            try:
                with urllib.request.urlopen(url) as f:
                    body = f.read()
            except Exception as e:
                print(e)
                break
            danmus = re.findall(r"\{.*\}", str(body, encoding='utf-8'))
            danmu = danmus[0]
            try:
                danmu_json = json.loads(danmu)
                if danmu_json["count"] == 0:
                    print("Section download finished: %s" % i)
                    break;
            except Exception as e:
                print(e)
                break
            try:
                danmu_collect["count"] += danmu_json["count"]
                danmu_collect["result"].extend(danmu_json["result"])
            except Exception as e:
                print(e)
                break
            j += 1
        res['videoId'] = json.dumps(danmu_collect, ensure_ascii=False)
        return res

    @staticmethod
    def danmu_download_file(line, ts=False):
        line_params = line.strip('\n').split('\t')
        print('Start process item: "%s".' % line.strip('\n'))
        if len(line_params) < 1:
            return False
        if not line_params[0].isdecimal():
            return False
        videoId = line_params[0]
        timestamp = time.strftime('%Y%m%d%H%M%S', time.localtime())
        res = danmu_diyidan_download.danmu_download(videoId)
        if 'videoId' in res:
            out_filename = videoId
            if ts:
                out_filename = out_filename + '_' + timestamp
            out_filename = out_filename + '.' + 'ykjson'
            try:
                with open(out_filename, mode='w', encoding='utf-8') as f:
                    f.write(res['videoId'])
                print('Success generate file: "%s".' % out_filename)
            except Exception as e:
                print(e)
