from module import *
from BeautifulReport import BeautifulReport

if len(sys.argv) > 1:
    project = sys.argv[1]  # 取出manage/teacher/assignment
    print('project:' + str(project))
    runmode = os.getenv('runmode')  # 接收的是跑case的类型：all，suites，single
    if runmode == 'suites':
        testcase = os.getenv('testcase').split(',')
    elif runmode == 'single':
        testcase = os.getenv('testcase')
    else:
        testcase = '*_test.py'
else:  # local
    project = 'teacher'
    runmode = 'single'  # 接收的是跑case的类型：all，suites，single
    if runmode == 'suites':
        testcase = 'Staff,Staff02,Project01,Project03'.split(',')
    elif runmode == 'single':
        testcase = 'addofflinescore_test.py'
    else:  # 'all'
        testcase = '*_test.py'


def run_testcase(test_dir):
    if runmode == 'single':
        discover = unittest.defaultTestLoader.discover(test_dir, pattern=testcase)
    elif runmode == 'suites':
        testloader = unittest.TestLoader()
        test_suite = []
        for cases in testcase:
            testSuite = testloader.loadTestsFromTestCase(eval(cases))  # 这里的eval有用到testcase.manage里的内容
            test_suite.append(testSuite)
        discover = unittest.TestSuite(test_suite)
    else:
        discover = unittest.defaultTestLoader.discover(test_dir, pattern=testcase)
    return discover


if __name__ == '__main__':
    run_path = './testcase/'
    if project in ('manage', 'teacher'):
        discover = run_testcase(run_path + project)
    else:
        discover = run_testcase(run_path)
    runner = BeautifulReport(discover).report(filename='tr_api_report', description='教研工作平台接口报告',
                                              log_path='./report/')
