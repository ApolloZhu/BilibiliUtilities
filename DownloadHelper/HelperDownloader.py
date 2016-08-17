# coding=utf-8
import urllib.request
import sys, os, zipfile, webbrowser

localization = {
    "notice":[
        "\033[2J\033[0;0H\n--[Product of Apollo Zhu from WWITDC]--\n\n"
        "Press `ENTER` to continue if you prefer using English\n"
        "默认界面语言为英文。若需要更改为中文，请输入 zh \n" # Translation: Language is default to English. enter `zh` to use Chinese
    ],
    "en":{
        "networkIssue": "Network issue",
        "sourceChanged": "The downlaod page has changed, developers are trying to solve this.\nPlease download the extension from {0}",
        "subject": "Bug of BBHelper Donwloader",
        "latestVersion": "Latest version: v",
        "confirmDownload": "Start to download? (y/n, or `ENTER` to start directly)",
        "downloadingProgress": "\033[17DDownloading: {0:3}%",
        "downloadError": "An error occured while downloading",
        "downloadCancel": "Cancelled downloading extension of versoin v{0}",
        "downloadComplete": "Download completed!",
        "unzip": "Start to unzip",
        "unzipError": "An error occured while unzipping",
        "unzipComplete": "Unzip completed",
        "fileLocation": "Downloaded file is named `{1}` in {0}"
    },
    "zh":{
        "networkIssue": "网络故障",
        "sourceChanged": "网页内容发生改变，开发者正在处理中\n请直接从 {0} 下载",
        "subject": "BiliBili助手下载器异常报告",
        "latestVersion": "当前最新版本: v",
        "confirmDownload": "是否需要下载? (y/n，或直接回车开始):",
        "downloadingProgress": "\033[14D下载进度：{0:3}%",
        "downloadError": "下载过程出现问题",
        "downloadCancel": "已取消下载 v {0} 版本的 BiliBili助手",
        "downloadComplete": "下载完成",
        "unzip": "开始解压",
        "unzipError": "解压过程出现问题",
        "unzipComplete": "解压完成",
        "fileLocation": "文件在 {0}，名字为 {1}"
    }
}
currentLanguage = "en"

def downloadProgressHandler(blockDownloadedCount, blockSize, totalSize):
    percentage = 100.0 * blockDownloadedCount * blockSize / totalSize
    if percentage >= 100:
        percentage = 100
    sys.stdout.write(localization[currentLanguage]["downloadingProgress"].format(int(percentage)))
    sys.stdout.flush()

def downloadBiliBiliHelper():
    sys.stdout.write("\033[2J\033[0;0H") # Clear screen
    try:
        link = "http://blackbili.nmzh.net/archives/bilibilihelper.html"
        with urllib.request.urlopen(link) as download: # Update posting page
            html = download.read().decode("utf-8")
            try:
                versionNumberLeft = html.index("更新 v") + 4
                versionNumberRight = html.index("来啦！")
                versionNumber = html[versionNumberLeft:versionNumberRight]
                print(localization[currentLanguage]["latestVersion"]+ versionNumber)
                print(localization[currentLanguage]["confirmDownload"], end=" ")
                response = input()
                if (response == "y" or response == ""):
                    try:
                        packageName = versionNumber + ".zip"
                        source = "http://download.sueri.cn/software/Helper" + packageName
                        packagePath = os.getcwd() + "/" + packageName
                        urllib.request.urlretrieve(source, packagePath, downloadProgressHandler)
                        print("\n\033[;32m" + localization[currentLanguage]["downloadComplete"] + "\033[0m")
                        print(localization[currentLanguage]["unzip"])
                        try:
                            extensionName = ".crx"
                            with zipfile.ZipFile(packageName, 'r') as package:
                                for name in package.namelist():
                                    if name.find(extensionName) > 0:
                                        extensionName = name;
                                        package.extract(extensionName)
                                        break
                            if os.path.exists(extensionName):
                                os.remove(packagePath)
                                print("\033[;32m" + localization[currentLanguage]["unzipComplete"] + "\033[0m")
                                print(localization[currentLanguage]["fileLocation"].format(os.getcwd(),extensionName))
                            else:
                                raise IOError
                        except:
                            print("\033[;31m" + localization[currentLanguage]["unzipError"] + "\033[0m")
                    except:
                       print("\033[;31m" + localization[currentLanguage]["downloadError"] + "\033[0m") 
                else:
                    print(localization[currentLanguage]["downloadCancel"].format(versionNumber))
                    return
            except:
                print("\033[;31m" + localization[currentLanguage]["sourceChanged"].format(link) + "\033[0m")
                webbrowser.open("mailto:public-apollonian@outlook.com?subject=" + localization[currentLanguage]["subject"])

    except:
        print("\033[;31m" + localization[currentLanguage]["networkIssue"] + "\033[0m")

# Main entry
for notice in localization["notice"]:
    print(notice)
print("=>", end=" ")
preferredLanguage = input()
if preferredLanguage in localization:
    currentLanguage = preferredLanguage
downloadBiliBiliHelper()
