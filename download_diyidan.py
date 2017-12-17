# !/usr/bin/python3
import sys
import os
import danmu_diyidan_download


def download_id(id):
    print('Start process id: "%s".' % id)
    danmu = danmu_diyidan_download.danmu_download(id)
    if danmu == None:
        return False
    out_filename = id + '.dydjson'
    try:
        with open(out_filename, mode='wb') as f:
            f.write(danmu)
    except Exception as e:
        print(e)
        return False
    print('Success generate file: "%s".' % out_filename)
    return True


def download_file(filename):
    print('Start process list file: "%s".' % filename)
    tmp_1 = os.path.splitext(filename)
    if tmp_1[1] == '.dydlist':
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
                danmu = danmu_diyidan_download.danmu_download(id)
                if danmu == None:
                    continue
                out_filename = id + '.dydjson'
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


def download_dir(dirname):
    print('Start process dir: "%s".' % dirname)
    for filename in os.listdir(dirname):
        if not os.path.isfile(filename):
            continue
        if os.path.splitext(filename)[1] != '.dydlist':
            continue
        download_file(filename)
    print('Success process dir: "%s".' % dirname)


if __name__ == '__main__':
    if len(sys.argv) > 1:
        for i in range(1, len(sys.argv)):
            argv_item = sys.argv[i]
            if argv_item.isdecimal():
                download_id(argv_item)
            elif os.path.isfile(argv_item):
                download_file(argv_item)
            elif os.path.isdir(argv_item):
                download_dir(argv_item)
    else:
        download_dir('.')
    os.system('pause')
