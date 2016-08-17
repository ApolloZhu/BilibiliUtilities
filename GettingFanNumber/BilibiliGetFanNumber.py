# coding=utf-8
import requests
import os
import json
import time
import threading
import encodings.idna
import warnings

os.system("cls")

currentFilePath = os.getcwd() + "/"

upListFileName = "VideoUploaderNameList"
fansCountFileName = "FansCount"
midListFileName = "midList"
batchCount = 49020
threadCount = 2040

preferenceFileName = currentFilePath + "settings.json"
if not os.path.exists(preferenceFileName):
    try:
        with open(preferenceFileName,"w",encoding="utf-8-sig") as preferenceFile:
            preferenceFile.write("""{
                "VideoUploaderNameList": "Uploaders",
                "FansCount": "FansNumberOfUploaders",
                "midList": "ValidUserIdentifierList",
                "threadsAtATime": 1500,
                "repeatingTimes": 66666
            }""")
    except:
        warnings.warn("Can't create preference file\n", IOError)

try:
    with open(preferenceFileName,"r", encoding="utf-8-sig") as preferenceFile:
        try:
            preference = json.load(preferenceFile)
            upListFileName = preference["VideoUploaderNameList"]
            fansCountFileName = preference["FansCount"]
            midListFileName = preference["midList"]
            threadCount = preference["threadsAtATime"]
            batchCount = preference["repeatingTimes"]
        except:
            warnings.warn("Error when loading preference\n", RuntimeError)
except:
    warnings.warn("Error when opening preference file\n",IOError)

date = time.strftime("-%Y-%m-%d_%H-%M-%S", time.localtime())
upListFileName = currentFilePath + upListFileName + date + ".txt"
fansCountFileName = currentFilePath + fansCountFileName + ".txt"
midListFileName = currentFilePath + midListFileName + ".txt"
try:
    with open(upListFileName, "w", encoding="utf-8-sig") as upListFile:
        print("Creating file for stroing UPs\n")
    with open(fansCountFileName,"w",encoding="utf-8-sig") as fansCountFile:
        print("Creating file for storing UPs with their fans count\n")
    with open(midListFileName,"w",encoding="utf-8-sig") as midListFile:
        print("Creating file for storing user identifier\n")
except:
    warnings.warn("Error when generating files for storing data \n", IOError)

def add(mid, user, fans):
    try:
        with open(fansCountFileName, "a", encoding="utf-8-sig") as fansCountFile:
            fansCountFile.write(str(mid) + ":" + str(user) + ":" + str(fans) + "\n")
    except:
        print("Can't write to ranking of " + str(mid) + ":" + str(user) + ":" + str(fans) + "\n")

    try:
        with open(upListFileName, "a", encoding="utf-8-sig") as upListFile:
            upListFile.write(str(user) + "\n")
    except:
        print("Can't write up with name" + user + "\n")

    try:
        with open(midListFileName, "a", encoding="utf-8-sig") as midListFile:
            midListFile.write(str(mid) + "\n")
    except:
        print("Can't add userID" + str(mid) + "\n")

def getUserInfoWithMid(mid):
    print("Starting Thread:" + str(mid) + "\n")
    url = "http://api.bilibili.cn/userinfo?mid=" + str(mid)
    try:
        response = requests.get(url)
        try:
            textContent = response.text
            jsonContent = json.loads(textContent)
            try:
                fans = jsonContent["fans"]
                name = jsonContent["name"]
                try:
                    add(mid, name,fans)
                except:
                    warnings.warn("IOError\n", IOError)
            except:
                pass
        except:
            warnings.warn("No valid JSON content with callback" + str(jsonContent) + "\n", RuntimeWarning)
    except:
        warnings.warn("Trying to access" + url + "again \n", RuntimeWarning)
        getUserInfoWithMid(mid)

threads = []
for batch in range(0,batchCount):
    threads = []
    for i in range(0,threadCount):
        mid = batch * threadCount + i
        thread = threading.Thread(name = mid, target=getUserInfoWithMid, args=(mid,))
        threads.append(thread)
    for thread in threads:
        succeed = False
        while not succeed:
            try:
                thread.start()
                succeed = True
            except:
                warnings.warn("Starting thread " + str(thread) + "again \n", RuntimeWarning)
                print("Please wait\n")
                threads[threads.index(thread) - 1].join()
    print("Please wait\n")
