# BilibiliUtilities
Many tools that relate to Bilibili.com

## DownloadHelper
![](https://img.shields.io/badge/language-Python3-blue.svg)

Download [bilibili-helper](https://github.com/zacyu/bilibili-helper) without need of accessing Google or viewing ***ads*** on [official update page](http://blackbili.nmzh.net/archives/bilibilihelper.html)

### Language supported
- English
- Chinese

***Localization are welcomed***

## GettingFanNumber
![](https://img.shields.io/badge/language-Python3-blue.svg) ![](https://img.shields.io/badge/dependencies-requests-blue.svg)

Get number of fans by the user identifier
***There are too many users, it's best to limit the range of the mid("User Identifier") so it will not take 3 month to get data of all users**

`段位统计` was inspired by [★⑥檤轮囬★](http://space.bilibili.com/295723/#!/index), though he never used it. It can get #fans of ups in `UP主列表.txt` and sort it

## BilibiliGetCoinNotification
![](https://img.shields.io/badge/language-Visual%20Basic-7D43AF.svg)

If you want auto collect and using Google Chrome as web browser, get helper using [`DownloadHelper`](https://github.com/WWITDC/BilibiliUtilities/blob/master/DownloadHelper/HelperDownloader.py) instead

### Supported System(s)
|x86|x64|
|:--:|:--:|
|![](https://img.shields.io/badge/win10-not%20tested-lightgrey.svg)|![](https://img.shields.io/badge/win10-passed-brightgreen.svg)|
|![](https://img.shields.io/badge/win8.1-not%20tested-lightgrey.svg)|![](https://img.shields.io/badge/win8.1-not%20tested-lightgrey.svg)|
|![](https://img.shields.io/badge/win8-not%20tested-lightgrey.svg)|![](https://img.shields.io/badge/win8-not%20tested-lightgrey.svg)|
|![](https://img.shields.io/badge/win7-passed-brightgreen.svg)|![](https://img.shields.io/badge/win7-not%20tested-lightgrey.svg)|
|![](https://img.shields.io/badge/vista-not%20tested-lightgrey.svg)|![](https://img.shields.io/badge/vista-not%20tested-lightgrey.svg)|
|![](https://img.shields.io/badge/xp-not%20tested-lightgrey.svg)|![](https://img.shields.io/badge/xp-not%20tested-lightgrey.svg)|

***Important***: Keyboard Hook is **not** available when testing with `Visual Studio`

`typealias Coin = "瓜子"`
Every 3, 6, 10 minutes, there will be `coin` available for [live.bilibili.com](live.bilibili.com).
This program pop up a MsgBox to notify you it is time to get those coins, so you don't have to stare at the live all the time
If you want to quit, use `Task Manager` or press `Windows`(master) Key
