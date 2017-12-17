import os


class danmu_download(object):
    def __init__(self, danmu_download, extname_danmu, extname_list):
        self.danmu_download = danmu_download
        self.extname_danmu = extname_danmu
        self.extname_list = extname_list

    def download_id(self, id):
        print('Start process id: "%s".' % id)
        danmu = self.danmu_download.danmu_download(id)
        if danmu == None:
            return False
        out_filename = id + '.' + self.extname_danmu
        try:
            with open(out_filename, mode='wb') as f:
                f.write(danmu)
        except Exception as e:
            print(e)
            return False
        print('Success generate file: "%s".' % out_filename)
        return True

    def download_file(self, filename):
        print('Start process list file: "%s".' % filename)
        tmp_1 = os.path.splitext(filename)
        if tmp_1[1] == '.' + self.extname_list:
            out_dir = tmp_1[0]
        else:
            out_dir = filename
        if not os.path.exists(out_dir):
            os.mkdir(out_dir)
        try:
            with open(filename, encoding='utf8') as f:
                for id in f:
                    id = id.strip('\n')
                    print('Start process id: "%s" in list file.' % filename)
                    if not id.isdecimal():
                        continue
                    danmu = self.danmu_download.danmu_download(id)
                    if danmu == None:
                        continue
                    out_filename = id + '.' + self.extname_danmu
                    try:
                        with open(os.path.join(out_dir, out_filename), mode='wb') as f2:
                            f2.write(danmu)
                    except Exception as e:
                        print(e)
                        continue
                    print('Success generate file: "%s" for id.' % out_filename)
        except Exception as e:
            print(e)
            return False
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
