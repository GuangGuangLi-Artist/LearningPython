# -*- coding: utf-8 -*-
import unittest
from unittest.suite import TestSuite
from parameterized import parameterized
'''
参数化
'''
data = [
    ('admin','123456','登陆成功'),
    ('admin','123123','登陆失败'),
    ('errorAdmin','123456','登陆失败'),
]
class ParameterizedTestCase(unittest.TestCase):
    
    @parameterized.expand(data)
    def test_login(self,username,password,expected):
        self.assertEqual(self.login(username,password),expected)
    
    def login(self,username,password):
        if username == 'admin' and password == '123456':
            return '登陆成功'
        else:
            return '登陆失败'

if __name__ == '__main__':
    unittest.main()