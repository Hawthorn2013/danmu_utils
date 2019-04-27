import os


__all__ = ['convert_file', 'convert_dir']


def convert_file(filename, tool):
    print('Start process file: "%s".' % filename)
    with open(filename, encoding='utf8') as f:
        danmu_diyidan = f.read()
    # Determine output file name
    tmp_1 = os.path.splitext(filename)
    if tmp_1[1] == '.' + tool.DANMU_EXTNAME_SRC:
        out_filename = tmp_1[0] + '.' + tool.DANMU_EXTNAME_DST
    else:
        out_filename = filename + '.' + tool.DANMU_EXTNAME_DST
    danmu_out = tool.convert(danmu_diyidan)
    with open(out_filename, mode='wb') as f:
        f.write(danmu_out)
    print('Success generate file: "%s".' % out_filename)


def convert_dir(dirname, tool):
    for filename in os.listdir(dirname):
        filename = os.path.join(dirname, filename)
        if not os.path.isfile(filename):
            continue
        if os.path.splitext(filename)[1] != '.' + tool.DANMU_EXTNAME_SRC:
            continue
        try:
            convert_file(filename, tool)
        except Exception as e:
            print(e)
            continue