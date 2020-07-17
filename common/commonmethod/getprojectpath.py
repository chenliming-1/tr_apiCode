#!Date：2018/12/4 11:48
# !@Author：龚远琪
from module import *


def getpath():
    filepath = os.path.abspath(os.path.dirname(__file__))
    # print("filepath:"+filepath)
    pro = re.search(r'tr_api.*?[/\\]', filepath).end()
    projectpath = filepath[:pro]
    return projectpath


projectpath = getpath()
# print(projectpath)
# print(os.path.dirname(os.path.abspath('.')))
# print(os.path.abspath(os.path.dirname(__file__)))
# print(os.path.abspath('.'))
# print(os.path.abspath(__file__))
# print(os.path.dirname(__file__))
# print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))