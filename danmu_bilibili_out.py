from xml.dom import minidom


def danmu_out(danmu_common):
    xml = minidom.Document()
    list = xml.createElement('i')
    xml.appendChild(list)
    for entry_common in danmu_common['list']:
        entry_bilibili = entry_out(entry_common)
        if (entry_bilibili == None):
            continue
        list.appendChild(entry_bilibili)
    danmu_bilibili = xml.toprettyxml(encoding='UTF-8')
    return danmu_bilibili

def entry_out(entry_common):
    xml = minidom.Document()
    try:
        entry_bilibili = xml.createElement('d')
        p = '%f,%d,%d,%d,%d,%d,%d,%d' % (
            entry_common['time'],  # 1. 弹幕发送相对视频的时间（以前是以秒为单位的整数，现在用浮点记了，更精准）
            1,  # 2. 弹幕类型：1~3（但貌似只见过1）滚动弹幕、4底端弹幕、5顶端弹幕、6逆向弹幕、7精准定位、8高级弹幕【默认是1，基本以1、4、5多见】
            25,  # 3. 字号：12非常小,16特小,18小,25中,36大,45很大,64特别大【默认是25】
            entry_common['color'],  # 4. 字体颜色：不是RGB而是十进制
            0,  # 5. 弹幕发送时的UNIX时间戳，基准时间1970-1-1 08:00:00
            0,  # 6. 弹幕池类型：0普通 1字幕 2特殊
            entry_common['sender'],  # 7. 发送者ID【注意不是uid，具体怎么关联的还不清楚，屏蔽用】
            0  # 8. 弹幕在数据库的ID
        )
        entry_bilibili.setAttribute('p', p)
        entry_bilibili.appendChild(xml.createTextNode(entry_common['text']))
    except Exception as e:
        print(e)
        return None
    return entry_bilibili