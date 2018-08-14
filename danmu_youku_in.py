import json


def danmu_in(danmu):
    try:
        danmu_diyidan = json.loads(danmu)
    except Exception as e:
        print(e)
        return None
    danmu_common = {'list': []}
    for entry_diyidan in danmu_diyidan['result']:
        entry_common = entry_in(entry_diyidan)
        if (entry_common == None):
            continue
        danmu_common['list'].append(entry_common)
    return danmu_common


def entry_in(entry):
    entry_common = {}
    try:
        entry_common['text'] = entry['content']
        entry_common['time'] = entry['playat'] / 1000
        propertis = json.loads(entry["propertis"])
        if "color" in propertis.keys():
            entry_common['color'] = int(propertis["color"])
        else:
            entry_common['color'] = 16777215
        entry_common['sender'] = entry['uid']
    except Exception as e:
        print(e)
        return None
    return entry_common
