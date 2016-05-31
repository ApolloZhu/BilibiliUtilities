#引用程序运行必要的文件
import os

#获取当前文件夹
currentFilePath = os.getcwd()

#新建UP主列表
with open(currentFilePath + "/UP主列表.txt","a",encoding="utf-8-sig") as upList:
    upList.write("★⑥檤轮囬★\nApollonian")

#配置文件
with open(currentFilePath + "/设置.txt","w",encoding="utf-8-sig") as preference:
    preference.write(
"""{
    "置顶显示": "★⑥檤轮囬★",
    "UP主列表文件名": "UP主列表",
    "结果输出主文件名": "段位表",
    "覆盖之前的文档": "否",
    "段位":[
        ["黄金", 300000],
        ["铂金", 400000],
        ["钻石", 500000],
        ["大师", 600000],
        ["王者", 700000]
    ]
}""")

#程序本体

#删除安装文件
#os.remove(currentFilePath + "/安装.py")

