#!Date：2019/2/14 10:35
# !@Author：龚远琪
from module import *
from commidware import *
import commidware.recognize.driver as dw
sys_name = "tr"


def getJenkinsData():
    if len(sys.argv) > 1:
        env = sys.argv[2]
        project = sys.argv[1]  # 取出manage/assignment/teacher
        print('project:' + str(project))
        runmode = os.getenv('runmode')  # 接收的是跑case的类型：all，suites，single
        if runmode == 'suites':
            testcase = os.getenv('testcase').split(',')
        elif runmode == 'single':
            testcase = os.getenv('testcase')
        else:
            testcase = '*_test.py'
    else:  # local
        env = 'test'
        project = 'teacher'
        runmode = 'all'  # 接收的是跑case的类型：all，suites，single
        if runmode == 'suites':
            testcase = 'Staff,Staff02,Project01,Project03'.split(',')
        elif runmode == 'single':
            testcase = 'addofflinescore_test.py'
        else:  # 'all'
            testcase = '*_test.py'
    return runmode, testcase, project, env


def GetUrl():
    runmode, testcase, project, env = getJenkinsData()
    sysURL = url.getSysUrl(sys_name, env, project)
    return sysURL, env


def Checkout_user(user_name, pwd, url):
    cookie = dw.get_login_driver(user_name, pwd, url)[1]
    return cookie


def GetDbName():
    runmode, testcase, project, env = getJenkinsData()
    sysdbname = dbname.getSysDbName(sys_name, env)
    return sysdbname


sysURL, env = GetUrl()
cookie = Checkout_user("gongyq", "111111", url=f'{sysURL}')
db = GetDbName()
