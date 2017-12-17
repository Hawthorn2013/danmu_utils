# !/usr/bin/python3
import sys
import os
import danmu_download
import danmu_bilibili_download

if __name__ == '__main__':
    danmu_download_1 = danmu_download.danmu_download(danmu_bilibili_download.danmu_bilibili_download(), 'xml',
                                                     'xmllist')
    if len(sys.argv) > 1:
        for i in range(1, len(sys.argv)):
            argv_item = sys.argv[i]
            if argv_item.isdecimal():
                danmu_download_1.download_id(argv_item)
            elif os.path.isfile(argv_item):
                danmu_download_1.download_file(argv_item)
            elif os.path.isdir(argv_item):
                danmu_download_1.download_dir(argv_item)
    else:
        danmu_download_1.download_dir('.')
    os.system('pause')
