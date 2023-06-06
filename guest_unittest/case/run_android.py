
from Androidtest import *
import unittest
from unittestreport import TestRunner


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(Test_Android('test_android_001'))
   # with open('./hTestReport.html','wb') as report:
   #   runnner=HTMLTestRunner(stream=report,title="bili 视频LIST",description="用例执行情况",verbosity=2)
    #runnner.run(suite)

    runnner = TestRunner(suite)
    runnner.run()