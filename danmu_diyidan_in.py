import json


def danmu_in(danmu):
    danmu_diyidan = json.loads(danmu)
    danmu_common = {'list': []}
    for entry_diyidan in danmu_diyidan['danmu']['danmakuList']:
        entry_common = {}
        entry_common['text'] = entry_diyidan['text']
        entry_common['time'] = entry_diyidan['time'] / 10
        entry_common['color'] = int(entry_diyidan['color'].split('#')[1], 16)
        entry_common['sender'] = entry_diyidan['danmakuId']
        danmu_common['list'].append(entry_common)
    return danmu_common
