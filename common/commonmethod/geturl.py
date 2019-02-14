#!Date：2019/2/14 10:35
#!@Author：龚远琪
from module import *
from commidware import *

def GetUrl():
    if len(sys.argv) > 1:
        project = sys.argv[1]  # 取出manage/assignment/teacher
    else:     #local#
        project = "teacher"
    return url.getSysUrl("tr", "at", project)

sysurl = GetUrl()