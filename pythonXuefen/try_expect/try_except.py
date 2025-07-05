#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import logging
logging.basicConfig(level=logging.INFO)  
import unittest
'''
错误处理
    try:
        code
    expect BaseException as e:
        logging || raise || print
    finally:
        code


1、记录错误:logging
2、抛出错误:raise

调试错误
    1、print()
    2、assert()
    3、logging()

单元测试
    1、编写单元测试时，我们需要编写一个测试类，从unittest.TestCase继承。
    2、以test开头的方法就是测试方法，不以test开头的方法不被认为是测试方法，测试的时候不会被执行
    3、对每一类测试都需要编写一个test_xxx()方法。由于unittest.TestCase提供了很多内置的条件判断，我们只需要调用这些方法就可以断言输出是否是我们所期望的。
'''

def foo(s):
    n = int(s)
    if n == 0:
        raise ValueError('not int')
    return 10 / 0

def bar():
    try:
        foo('0')
    except:
        logging.exception('cuole')
        raise ZeroDivisionError
    finally:
        (print('胡求整'))

def foo_ass(s):
    n = int(s)
    logging.info('n = %d' % n)
    assert n != 0,'n is zero'
    return 10 / n


class Stu_unittest():
    def __init__(self, name, score):
        self.name = name
        self.score = score
    def get_grade(self):
        if self.score > 100 or self.score < 0:
            raise ValueError('分数应在0-100之间')
        if self.score >= 60 and self.score < 80:
            return 'B'
        if self.score >= 80 and self.score <=100:
            return 'A'
        return 'C'
class TestStu_unittest(unittest.TestCase):
    def test_80_to_100(self):
        s1 = Stu_unittest('Bart',80)
        s2 = Stu_unittest('Lisa',100)
        self.assertEqual(s1.get_grade(),'A')
        self.assertEqual(s2.get_grade(),'A')
    
    def test_60_to_80(self):
        s1 = Stu_unittest('Bart',60)
        s2 = Stu_unittest('Lisa',79)
        self.assertEqual(s1.get_grade(),'B')
        self.assertEqual(s2.get_grade(),'B')

    def test_0_to_60(self):
        s1 = Stu_unittest('Bart',0)
        s2 = Stu_unittest('Lisa',59)
        self.assertEqual(s1.get_grade(),'C')
        self.assertEqual(s2.get_grade(),'C')
    
    def test_invalid(self):
        s1 = Stu_unittest('Bart',-1)
        s2 = Stu_unittest('Lisa',101)
        with self.assertRaises(ValueError):
            s1.get_grade()
        with self.assertRaises(ValueError):
            s2.get_grade()
class TestDict(unittest.TestCase):
    def setUp(self):
        print('setUp')
    def tearDown(self):
        print('tearDown')

if __name__ == '__main__':
    #bar() 
    s = '1'
    if s == '0':
        foo_ass('0')
    unittest.main()


    