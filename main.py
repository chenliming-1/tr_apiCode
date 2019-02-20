from module import *
from BeautifulReport import BeautifulReport
from common.commonmethod import getjendata_url_cookie

runmode, testcase, project, env = getjendata_url_cookie.getJenkinsData()
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
    if project in ('manage', 'assignment', 'teacher'):
        discover = run_testcase(run_path + project)
    else:
        discover = run_testcase(run_path)
    runner = BeautifulReport(discover).report(filename='tr_api', description='教研平台接口测试报告',
                                              log_path='./report/')