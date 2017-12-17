# !/usr/bin/python3
import sys
import os
import danmu_diyidan_in
import danmu_bilibili_out


def convert_file(filename):
    print('Start process file: "%s".' % filename)
    try:
        with open(filename, encoding='utf8') as f:
            danmu_diyidan = f.read()
    except Exception as e:
        print(e)
        return False
    danmu_common = danmu_diyidan_in.danmu_in(danmu_diyidan)
    if danmu_common == None:
        return False
    danmu_bilibili = danmu_bilibili_out.danmu_out(danmu_common)
    if danmu_bilibili == None:
        return False
    # Determine output file name
    tmp_1 = os.path.splitext(filename)
    if tmp_1[1] == '.dydjson':
        out_filename = tmp_1[0] + '.xml'
    else:
        out_filename = filename + '.xml'
    try:
        with open(out_filename, mode='wb') as f:
            f.write(danmu_bilibili)
    except Exception as e:
        print(e)
        return False
    print('Success generate file: "%s".' % out_filename)
    return True


def convert_dir(dirname):
    for filename in os.listdir(dirname):
        if not os.path.isfile(filename):
            continue
        if os.path.splitext(filename)[1] != '.dydjson':
            continue
        convert_file(filename)


if __name__ == '__main__':
    if len(sys.argv) > 1:
        for i in range(1, len(sys.argv)):
            argv_item = sys.argv[i]
            if os.path.isfile(argv_item):
                convert_file(argv_item)
            elif os.path.isdir(argv_item):
                convert_dir(argv_item)
    else:
        convert_dir('.')
    os.system('pause')
