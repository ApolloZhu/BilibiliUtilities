# BilibiliUtilities
Many tools relating to [Bilibili](bilibili.com)

## Download Helper
![](https://img.shields.io/badge/language-Python3-blue.svg)

Download compiled [bilibili-helper](https://github.com/zacyu/bilibili-helper) without need of accessing Google or viewing ***ads*** on [official update page](http://blackbili.nmzh.net/archives/bilibilihelper.html)

### Language supported
- English
- Chinese

***Localization are welcomed***

## Get Fan Number
![](https://img.shields.io/badge/language-Python3-blue.svg) ![](https://img.shields.io/badge/dependencies-requests-blue.svg)

Get number of fans by the user identifier
There are too many users, it's best to **limit the range of the mid("User Identifier")** so it will not take 3 month to get data of all users

`段位统计` was inspired by [★⑥檤轮囬★](http://space.bilibili.com/295723/#!/index), though he never used it. It can get #fans of ups in `UP主列表.txt` and sort it

## Notify Getting Coin
![](https://img.shields.io/badge/language-Visual%20Basic-7D43AF.svg) [![](https://img.shields.io/badge/.Net%20Framework-3.5+-blue.svg)](https://www.microsoft.com/en-us/download/details.aspx?id=22)

If you want auto collect and using Google Chrome as web browser, get helper using [`DownloadHelper`](https://github.com/WWITDC/BilibiliUtilities/blob/master/DownloadHelper/HelperDownloader.py) instead

### Supported Systems
||x86|x64|
|:--:|:--:|:--:|
|10|![](https://img.shields.io/badge/status-support-brightgreen.svg)|![](https://img.shields.io/badge/status-support-brightgreen.svg)|
|8.1|![](https://img.shields.io/badge/status-not%20tested-lightgrey.svg)|![](https://img.shields.io/badge/status-should%20support-green.svg)|
|8|![](https://img.shields.io/badge/status-should%20support-green.svg)|![](https://img.shields.io/badge/status-should%20support-green.svg)|
|7|![](https://img.shields.io/badge/status-should%20support-yellow.svg)|![](https://img.shields.io/badge/status-not%20tested-lightgrey.svg)|
|vista|![](https://img.shields.io/badge/status-not%20tested-lightgrey.svg)|![](https://img.shields.io/badge/status-not%20tested-lightgrey.svg)|
|xp|![](https://img.shields.io/badge/status-support-brightgreen.svg)|![](https://img.shields.io/badge/status-support-brightgreen.svg)|

***Important***: Keyboard Hook is **not** available when testing within `Visual Studio`

`typealias Coin = "银瓜子"`

Every `{3, 6, 10}` minutes, there will be `coin` available for [live.bilibili.com](live.bilibili.com).
This program pop up a `MsgBox` to notify you it is time to get those coins, so you don't have to stare at the live all the time
### Quit Application
Since it runs in the background, you need to use one of the ways listed below
- press `Windows(master)` key
- use `Task Manager`
