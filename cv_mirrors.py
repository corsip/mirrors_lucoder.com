# coding=UTF-8
import os,sys

def executeWithSudo(cmd,pms):
    os.system("echo {} | sudo -S {}".format(pms["sudo"],cmd))
def execute(cmd,pms): 
    os.system(cmd)
def fixDependency(pms):
    executeWithSudo("yum install -y aria2 dos2unix",pms)

def downloadFiles(pms):
    for link in pms["links"]:
        subDir = getDirName(link)
        dir = "{}{}".format(pms["dir"],subDir)
        if os.path.exists(dir) == False :
            os.makedirs(dir)
        os.system("aria2c -s 4 -c -l {} -d {}".format(link,dir))

def getDirName(item):
    firstIndex = item.find("/opencv")
    lastIndex = item.rfind("/")
    subItem = item[firstIndex:lastIndex + 1]
    return subItem

def readLinks(pms):
    lines = []
    with open(pms["lines"]) as reader:
        linesx = reader.readlines()
        for item in linesx:
            if item.find("#") > 0 or len(item) <= 0:
                continue
            lines.append(item.strip('\n'))    
    return lines

def printHtml(pms):
    html = "<!DOCTYPE html><html lang=\"en\"><head><meta charset=\"UTF-8\"><title>牧轩镜像站</title></head><body><h2>本服务常年运行，旨在加速国内OpenCV文件下载，具体访问：<a href=\"https://go.lucoder.com/fwlink/?linkid=5\">牧轩镜像站</a>了解更多信息！</h2></body></html>"
    wwwroot = "{}/index.html".format(pms["dir"])
    with open(wwwroot,"w") as writer:
        writer.write(html)

def run(pms):
    fixDependency(pms)
    lines = readLinks(pms)
    pms["links"] = lines
    downloadFiles(pms)
    printHtml(pms)

pms = {
    "sudo":"123456",
    "dir":"/www/wwwroot/mirrors.lucoder.com",
    "lines":"links.txt",
    "links":[]
}
run(pms)