# !/usr/bin/python3
import sys
import os
import danmu_diyidan_download
import cmdparam_download

if __name__ == '__main__':
    danmu_download_1 = cmdparam_download.cmdparam_download(danmu_diyidan_download.danmu_diyidan_download(),
                                                           'dydjson',
                                                           'dydlist')
    if len(sys.argv) > 1:
        danmu_download_1.parse_cmd_params(sys.argv[1:])
    else:
        danmu_download_1.download_dir(['.',])
    os.system('pause')
