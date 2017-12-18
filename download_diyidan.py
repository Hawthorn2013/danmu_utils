# !/usr/bin/python3
import sys
import os
import danmu_diyidan_download
import cmdparam_download

if __name__ == '__main__':
    danmu_download_1 = cmdparam_download.cmdparam_download(danmu_diyidan_download.danmu_diyidan_download(param='videoId'),
                                                     'dydjson',
                                                     'dydlist')
    if len(sys.argv) > 1:
        for i in range(1, len(sys.argv)):
            argv_item = sys.argv[i]
            if os.path.isfile(argv_item):
                danmu_download_1.download_file(argv_item)
            elif os.path.isdir(argv_item):
                danmu_download_1.download_dir(argv_item)
            else:
                danmu_download_1.download_item(argv_item)
    else:
        danmu_download_1.download_dir('.')
    os.system('pause')
