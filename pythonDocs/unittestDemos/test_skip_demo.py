# -*- coding: utf-8 -*-
import unittest
from unittest.suite import TestSuite
from BeautifulReport import BeautifulReport
import time
import logging
import os

# 配置日志系统
def setup_logging():
    """设置日志配置"""
    # 创建日志目录（如果不存在）
    log_dir = "test_logs"
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)
    
    # 生成带时间戳的日志文件名
    timestamp = time.strftime("%Y%m%d_%H%M%S")
    log_filename = os.path.join(log_dir, f"test_execution_{timestamp}.log")
    
    # 配置日志
    logging.basicConfig(
        level=logging.INFO,  # 设置日志级别
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',  # 日志格式
        handlers=[
            logging.FileHandler(log_filename, encoding='utf-8'),  # 文件处理器，输出到文件
            logging.StreamHandler()  # 流处理器，输出到控制台
        ]
    )
    
    return log_filename

class TestSkipDemo(unittest.TestCase):
    # 获取当前类的日志器
    logger = logging.getLogger(__name__)

    @classmethod
    def setUpClass(cls):
        cls.logger.info("setUpClass: 在所有测试方法执行前运行一次")
        print("setUpClass: 在所有测试方法执行前运行一次")
    
    @classmethod
    def tearDownClass(cls):
        cls.logger.info("tearDownClass: 在所有测试方法执行后运行一次")
        print("tearDownClass: 在所有测试方法执行后运行一次")
    
    def setUp(self):
        self.logger.info("setUp: 在每个测试方法执行前运行")
        print("setUp: 在每个测试方法执行前运行")

    def tearDown(self):
        self.logger.info("tearDown: 在每个测试方法执行后运行")
        print("tearDown: 在每个测试方法执行后运行")
    
    @unittest.skip("跳过此测试方法")
    def test_skip_method(self):
        self.logger.info("这个测试方法被跳过，不会执行")
        print("这个测试方法被跳过，不会执行")
        self.assertEqual(1, 1)

    @unittest.skipIf(2 > 1, "条件为真，跳过此测试方法")
    def test_skip_if(self):
        self.logger.info("这个测试方法被条件跳过，不会执行")
        print("这个测试方法被条件跳过，不会执行")
        self.assertEqual(1, 1)

    @unittest.skipUnless(1 > 2, "条件为假，跳过此测试方法")
    def test_skip_unless(self):
        self.logger.info("这个测试方法被条件跳过，不会执行")
        print("这个测试方法被条件跳过，不会执行")
        self.assertEqual(1, 1)

    @unittest.expectedFailure
    def test_expected_failure(self):
        self.logger.info("这个测试方法预期会失败")
        print("这个测试方法预期会失败")
        self.logger.warning("故意让测试失败：1 != 0")
        self.assertEqual(1, 0)  # 故意让测试失败

if __name__ == '__main__':
    # 设置日志并获取日志文件路径
    log_file = setup_logging()
    logger = logging.getLogger(__name__)
    logger.info("开始执行测试套件")
    
    # 1. 创建测试套件
    suite = TestSuite()
    logger.info("测试套件创建完成")
    
    # 2. 将测试用例添加到套件中
    test_cases = [
        "test_skip_method",
        "test_skip_if", 
        "test_skip_unless",
        "test_expected_failure"
    ]
    
    for test_case in test_cases:
        suite.addTest(TestSkipDemo(test_case))
        logger.info(f"添加测试用例: {test_case}")
    
    logger.info(f"共添加 {len(test_cases)} 个测试用例到套件中")
    
    # 3. 生成带时间戳的报告文件名，避免覆盖
    timestamp = time.strftime("%Y%m%d_%H%M%S")
    report_filename = f"Test_Report_{timestamp}.html"
    logger.info(f"测试报告将保存为: {report_filename}")
    
    try:
        # 4. 使用HTMLTestRunner运行测试并生成报告
        result = BeautifulReport(suite)
        result.report(filename=report_filename, description="跳过测试示例报告", log_path=".")
        logger.info("测试运行完成，报告生成成功")
        
            
    except Exception as e:
        logger.error(f"执行测试时发生错误: {str(e)}", exc_info=True)
        raise
    
    finally:
        logger.info(f"测试报告已生成: {report_filename}")
        logger.info(f"详细日志已保存: {log_file}")
        print(f"测试报告已生成: {report_filename}")
        print(f"详细日志已保存: {log_file}")