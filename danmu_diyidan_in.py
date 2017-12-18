import json


def danmu_in(danmu):
    try:
        danmu_diyidan = json.loads(danmu)
    except Exception as e:
        print(e)
        return None
    danmu_common = {'list': []}
    for entry_diyidan in danmu_diyidan['data']['danmakuList']:
        entry_common = entry_in(entry_diyidan)
        if (entry_common == None):
            continue
        danmu_common['list'].append(entry_common)
    return danmu_common


def entry_in(entry):
    entry_common = {}
    if 'text' in entry:
        try:
            entry_common['text'] = entry['text']
            entry_common['time'] = entry['time'] / 10
            entry_common['color'] = int(entry['color'].split('#')[1], 16)
            entry_common['sender'] = entry['danmakuId']
        except Exception as e:
            print(e)
            return None
    elif 'danmakuContent' in entry:
        try:
            entry_common['text'] = entry['danmakuContent']
            entry_common['time'] = entry['danmakuTime'] / 1000
            entry_common['color'] = entry['danmakuTextColor']
            entry_common['sender'] = entry['danmakuId']
        except Exception as e:
            print(e)
            return None
    else:
        return None
    return entry_common
