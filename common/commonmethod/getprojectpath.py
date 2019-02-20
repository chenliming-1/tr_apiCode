#!Date：2018/12/4 11:48
# !@Author：龚远琪

from module import *

def getpath():
    filepath = os.path.abspath(os.path.dirname(__file__))
    pro = re.search(r'tr_api.*?[/\\]', filepath).end()
    projectpath = filepath[:pro]
    return projectpath

projectpath = getpath()