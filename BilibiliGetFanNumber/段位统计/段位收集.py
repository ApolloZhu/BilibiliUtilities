# coding=utf-8
import requests
import os
import json
import warnings
import time
from operator import itemgetter

os.system("cls")

currentFilePath = os.getcwd() + "/"

users = []
results = []
error = []
outputString = ""
inputFileName = "UP主列表"
outputMainFileName = "段位表"
segementation = []
overwrite = True
top = "★⑥檤轮囬★"

with open(currentFilePath + "设置.txt","r", encoding="utf-8-sig") as preferenceFile:
    preference = json.load(preferenceFile)
    if preference["覆盖之前的文档"] == "否":
        overwrite = False
    top = preference["置顶显示"]
    inputFileName = preference["UP主列表文件名"]
    outputMainFileName = preference["结果输出主文件名"]
    segementation = preference["段位"]
    
with open(currentFilePath + inputFileName + ".txt", "r", encoding="utf-8-sig") as inputFile:
    fileContent = inputFile.read().replace(" ","")
    users = fileContent.split('\n')
    print("正在清楚重复的UP主")
    users = list(set(users))

for user in users:
    if not user == "":
        print("正在读取:", user)
        url = "http://api.bilibili.cn/userinfo?user=" + user
        response = requests.get(url)
        textContent = response.text
        try:
            leftFansIndex = textContent.index("\"fans\"") + 7
            rightFansIndex = textContent.index(",\"friend\"")
            results.append((user, int(textContent[leftFansIndex:rightFansIndex])))
        except:
            warnings.warn("读取" + user + "的信息时出错")
            error.append("读取" + user + "的信息时出错")
            
print("正在排位")
results = sorted(results, key=itemgetter(1), reverse = True)
if segementation:
    segementation = sorted(segementation, key=itemgetter(1), reverse = True)
    level = 0
    index = 0
    currentStandard = segementation[level][1]
    haveUserInCurrentLevel = False
    segementTitle = segementation[level][0] + "段"
    outputString = outputString + segementTitle +"(>="+str(segementation[level][1])+")\n"
    for result in results:
        fans = result[1]
        if result[1] >= currentStandard:
            haveUserInCurrentLevel = True
            outputString = outputString + result[0] + ":" + str(fans) + "\n"
            index += 1
        else:
            while True:
                if not haveUserInCurrentLevel:
                    outputString = outputString + "无\n"
                haveUserInCurrentLevel = False
                level = level + 1
                currentLevelUsers = []
                try:
                    currentStandard = segementation[level][1]
                    segementTitle = segementation[level][0] + "段"
                    outputString = outputString + "\n" + segementTitle +"("+str(segementation[level -1][1])+"-"+str(segementation[level][1])+")\n"
                except:
                    currentStandard = 0
                    segementTitle = "未进入排位部分"
                    outputString = outputString + "\n"+ segementTitle+"("+str(segementation[level -1][1])+"-0)\n"
                if fans > currentStandard:
                    outputString = outputString + result[0] + ":" + str(fans) + "\n"
                    haveUserInCurrentLevel = True
                    index += 1
                    break
        if result[0] == top:
            outputString = top+" 在所有列出的UP中排第"+str(index)+"位,粉丝"+str(fans)+"位，位于"+segementTitle+"\n\n"+ outputString
                
                
else:
    for result in results:
        outputString = outputString + result[0] + ':' + str(result[1]) + "\n"
    
outputFileName = currentFilePath + outputMainFileName
if not overwrite:
    # -年-月-日_时-分-秒
    date = time.strftime("-%Y-%m-%d_%H-%M-%S", time.localtime())
    outputFileName = outputFileName + date

with open(outputFileName + ".txt","w", encoding="utf-8-sig") as outputFile:
        outputFile.write(outputString)

if error:
    date = time.strftime("-%Y-%m-%d_%H-%M-%S", time.localtime())
    with open(currentFilePath + "错误"+date+".txt","w", encoding="utf-8-sig") as errorFile:
        errorFile.write(('\n'.join(error)))
