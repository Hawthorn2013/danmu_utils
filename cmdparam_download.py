import os


class cmdparam_download(object):
    def __init__(self, danmu_download, extname_danmu, extname_list):
        self.danmu_download = danmu_download
        self.extname_danmu = extname_danmu
        self.extname_list = extname_list

    def download_item(self, item):
        self.danmu_download.danmu_download_file(item)

    def download_file(self, filename):
        print('Start process list file: "%s".' % filename)
        tmp_1 = os.path.splitext(filename)
        if tmp_1[1] == '.' + self.extname_list:
            out_dir = tmp_1[0]
        else:
            out_dir = filename
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
