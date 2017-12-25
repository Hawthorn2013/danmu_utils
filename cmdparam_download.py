import os
import time


class cmdparam_download(object):
    param_timestamp_dir = False
    param_timestamp_file = False

    def __init__(self, danmu_download, extname_danmu, extname_list):
        self.danmu_download = danmu_download
        self.extname_danmu = extname_danmu
        self.extname_list = extname_list

    def download_item(self, item):
        self.danmu_download.danmu_download_file(item, ts=self.param_timestamp_file)

    def download_file(self, filename):
        print('Start process list file: "%s".' % filename)
        tmp_1 = os.path.splitext(filename)
        if tmp_1[1] == '.' + self.extname_list:
            out_dir = tmp_1[0]
        else:
            out_dir = filename
        if self.param_timestamp_dir:
            timestamp = time.strftime('%Y%m%d%H%M%S', time.localtime())
            out_dir = out_dir + '_' + timestamp
        if not os.path.exists(out_dir):
            os.mkdir(out_dir)
        curdir = os.path.abspath(os.curdir)
        try:
            with open(filename, encoding='utf8') as f:
                os.chdir(out_dir)
                for line in f:
                    self.download_item(line)
        except Exception as e:
            print(e)
            return False
        os.chdir(curdir)
        print('Success generate dir: "%s" for list file.' % out_dir)
        return True

    def download_dir(self, dirname):
        print('Start process dir: "%s".' % dirname)
        for filename in os.listdir(dirname):
            if not os.path.isfile(filename):
                continue
            if os.path.splitext(filename)[1] != '.' + self.extname_list:
                continue
            self.download_file(filename)
        print('Success process dir: "%s".' % dirname)

    def parse_cmd_params(self, params):
        list_listfiles = []
        list_listfilesdirs = []
        list_items = []
        i = 0
        while i < len(params):
            if params[i][0] == '-':
                if params[i] == '-tsd':
                    self.param_timestamp_dir = True
                elif params[i] == '-tsf':
                    self.param_timestamp_file = True
                else:
                    print('Invalid param: "%s"' % params[i])
                    exit(1)
            else:
                if os.path.isfile(params[i]):
                    list_listfiles.append(params[i])
                elif os.path.isdir(params[i]):
                    list_listfilesdirs.append(params[i])
                else:
                    list_items.append(params[i])
            i = i + 1
        for item in list_items:
            self.download_item(item)
        for file in list_listfiles:
            self.download_file(file)
        for dir in list_listfilesdirs:
            self.download_dir(dir)
