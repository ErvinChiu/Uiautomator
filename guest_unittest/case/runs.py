# _*_coding:utf-8_*_
# @Time    :2021/12/115:51
# @Author  :ErvinChiu
# @Email   :ErvinChiu@outlook.com
# @File    :runs.py
# @Sofeware:PyCharm
import unittest
from BeautifulReport import BeautifulReport  # 导入BeautifulReport

if __name__ == '__main__':
    suite_tests = unittest.defaultTestLoader. \
        discover(".", pattern="*event.py", top_level_dir=None)  # "."表示当前目录，"*tests.py"匹配当前目录下所有tests.py结尾的用例
    BeautifulReport(suite_tests).report(filename='测试报告', description='接口自动化测试',log_path='.',theme='theme_candy')  # log_path='.'把report放到当前目录下_dir=None) #"."表示当前目录，"*event.py"匹配当前目录下所有tests.py结尾的用例    BeautifulReport(suite).report(filename='测试报告', description='测试', log_path='.')    #log_path='.'把report放到当前目录下
