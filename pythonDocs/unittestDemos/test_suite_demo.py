# -*- coding: utf-8 -*-
import unittest
from unittest.suite import TestSuite
import HtmlTestRunner

class TestDemo1(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("setUpClass: 在所有测试方法执行前运行一次")
    
    @classmethod
    def tearDownClass(cls):
        print("tearDownClass: 在所有测试方法执行后运行一次")
    
    
    def setUp(self):
        print("setUp: 在每个测试方法执行前运行")

    def tearDown(self):
        print("tearDown: 在每个测试方法执行后运行")
    
    
    
    def test_subtraction1(self):
        print("执行 test_subtraction1")
        self.assertEqual(2 - 1, 1)
    
    def test_subtraction2(self):
        print("执行 test_subtraction2")
        self.assertEqual(5 - 3, 2)

if __name__ == '__main__':
    # 创建测试套件
    suite = TestSuite()
    # 添加测试用例到测试套件
    suite.addTest(TestDemo1("test_subtraction1"))
    suite.addTest(TestDemo1("test_subtraction2"))
    
    # 移除了 TextTestRunner 的运行部分，避免错误
    runner = unittest.TextTestRunner()
    runner.run(suite)
    
    # 生成HTML测试报告
    # with open("test_report.html", "wb") as report_file:
    #     html_runner = HtmlTestRunner.HTMLTestRunner(
    #         stream=report_file,
    #         report_title="测试报告",
    #         descriptions="测试减法运算",  # 将 descriptions=True 修改为字符串描述
    #         verbosity=2
    #     )
    #     html_runner.run(suite)
    # print("测试报告已生成: test_report.html")