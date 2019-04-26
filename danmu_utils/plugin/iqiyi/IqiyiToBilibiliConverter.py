import json
from xml.dom import minidom
from danmu_utils.common.IConverter import IConverter


class IqiyiToBilibiliConverter(IConverter):
    @property
    def DANMU_TYPE_SRC(self):
        return 'iqiyi'

    @property
    def DANMU_TYPE_DST(self):
        return 'bilibili'

    @property
    def DANMU_EXTNAME_SRC(self):
        return 'iqyxml'

    @property
    def DANMU_EXTNAME_DST(self):
        return 'xml'

    def _convert_entry(self, entry):
        dst_text = entry.getElementsByTagName('content')[0].childNodes[0].nodeValue
        dst_time = float(entry.getElementsByTagName('showTime')[0].childNodes[0].nodeValue)
        dst_color = int(entry.getElementsByTagName('color')[0].childNodes[0].nodeValue, 16)
        dst_sender = int(entry.getElementsByTagName('userInfo')[0].getElementsByTagName('uid')[0].childNodes[0].nodeValue)
        xml = minidom.Document()
        dst_entry = xml.createElement('d')
        p = '%f,%d,%d,%d,%d,%d,%d,%d' % (
            dst_time,  # 1. 弹幕发送相对视频的时间（以前是以秒为单位的整数，现在用浮点记了，更精准）
            1,  # 2. 弹幕类型：1~3（但貌似只见过1）滚动弹幕、4底端弹幕、5顶端弹幕、6逆向弹幕、7精准定位、8高级弹幕【默认是1，基本以1、4、5多见】
            25,  # 3. 字号：12非常小,16特小,18小,25中,36大,45很大,64特别大【默认是25】
            dst_color,  # 4. 字体颜色：不是RGB而是十进制
            0,  # 5. 弹幕发送时的UNIX时间戳，基准时间1970-1-1 08:00:00
            0,  # 6. 弹幕池类型：0普通 1字幕 2特殊
            dst_sender,  # 7. 发送者ID【注意不是uid，具体怎么关联的还不清楚，屏蔽用】
            0  # 8. 弹幕在数据库的ID
        )
        dst_entry.setAttribute('p', p)
        dst_entry.appendChild(xml.createTextNode(dst_text))
        return dst_entry

    def convert(self, data):
        item_src = minidom.parseString(data)
        xml = minidom.Document()
        list = xml.createElement('i')
        xml.appendChild(list)
        for entry_src in item_src.getElementsByTagName('danmu')[0].getElementsByTagName('data')[0].getElementsByTagName('entry'):
            for bullet_info in entry_src.getElementsByTagName('list')[0].getElementsByTagName('bulletInfo'):
                try:
                    entry_dst = self._convert_entry(bullet_info)
                except Exception as e:
                    print(e)
                    continue
                list.appendChild(entry_dst)
        item_dst = xml.toprettyxml(encoding='UTF-8')
        return item_dst


from danmu_utils.common.plugin_collection import add_convert_tool

add_convert_tool(IqiyiToBilibiliConverter().DANMU_TYPE_SRC, IqiyiToBilibiliConverter().DANMU_TYPE_DST, IqiyiToBilibiliConverter)
