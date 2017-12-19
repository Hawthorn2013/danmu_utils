# danmu_utils

danmu_utils is a tool to download danmu and convert danmu format.

download_*.py can download danmu from *, now it can download danmu from bilibili and diyidan.

convert_A_to_B.py can convert danmu from format A to B, now it can convert diyidan format to bilibili format.

other *.py is internal script, users will not use them directly.

Extfilename   Description

xmllist       bilibili danmu list to download

dydlist       diyidan danmu list to download

xml           bilibili danmu file

dydjson       diyidan danmu file

Every line in *.xxxlist is a item to download.

Every line in *.xmllist is the cid of danmu of bilibili.

Every line in *.dydlist is the 'videoId\tpostId' of danmu of bilibili.

py download_bilibili.py xxx.xmllist

py download_diyidan.py xxx.dydlist

py convert_diyidan_to_bilibili.py xxx.dydjson
