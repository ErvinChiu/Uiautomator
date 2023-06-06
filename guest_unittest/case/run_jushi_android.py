
from toast_test import *
import unittest
from unittestreport import TestRunner

from HTMLTestRunnerNew import HTMLTestRunner
if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(Test_login('test_login_001'))
    with open('./hTestReport.html','wb') as report:
        runnner=HTMLTestRunner(stream=report,title="bili 视频LIST",description="用例执行情况",verbosity=2)
        runnner.run(suite)

    # runnner = TestRunner(suite)
    # runnner.run()