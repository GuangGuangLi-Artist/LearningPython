# -*- coding: utf-8 -*-
import unittest

class TestDemo2(unittest.TestCase):
    
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

    def test_addition1(self):
        print("执行 test_addition")
        self.assertEqual(1 + 1, 2)
    
    def test_addition2(self):
        print("执行 test_addition2")
        self.assertEqual(2 + 2, 4)

if __name__ == '__main__':
    unittest.main()