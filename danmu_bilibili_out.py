from xml.dom import minidom


def danmu_out(danmu_common):
    xml = minidom.Document()
    root = xml.createElement('i')
    xml.appendChild(root)
    # node = xml.createElement('chatserver')
    # node.appendChild(xml.createTextNode('chat.bilibili.com'))
    # root.appendChild(node)
    # node = xml.createElement('chatid')
    # node.appendChild(xml.createTextNode('0'))
    # root.appendChild(node)
    # node = xml.createElement('mission')
    # node.appendChild(xml.createTextNode('0'))
    # root.appendChild(node)
    # node = xml.createElement('maxlimit')
    # node.appendChild(xml.createTextNode('3000'))
    # root.appendChild(node)
    # node = xml.createElement('source')
    # node.appendChild(xml.createTextNode('e-r'))
    # root.appendChild(node)
    for entry_common in danmu_common['list']:
        node = xml.createElement('d')
        p = '%f,%d,%d,%d,%d,%d,%d,%d' % (
            entry_common['time'],  # 1. 弹幕发送相对视频的时间（以前是以秒为单位的整数，现在用浮点记了，更精准）
            1,  # 2. 弹幕类型：1~3（但貌似只见过1）滚动弹幕、4底端弹幕、5顶端弹幕、6逆向弹幕、7精准定位、8高级弹幕【默认是1，基本以1、4、5多见】
            25,  # 3. 字号：12非常小,16特小,18小,25中,36大,45很大,64特别大【默认是25】
            entry_common['color'],  # 4. 字体颜色：不是RGB而是十进制
            0,  # 5. 弹幕发送时的UNIX时间戳，基准时间1970-1-1 08:00:00
            0,  # 6. 弹幕池类型：0普通 1字幕 2特殊
            entry_common['sender'],  # 7. 发送者ID【注意不是uid，具体怎么关联的还不清楚，屏蔽用】
            8  # 8. 弹幕在数据库的ID
        )
        node.setAttribute('p', p)
        node.appendChild(xml.createTextNode(entry_common['text']))
        root.appendChild(node)

    danmu_bilibili = xml.toprettyxml(encoding='UTF-8')
    return danmu_bilibili
