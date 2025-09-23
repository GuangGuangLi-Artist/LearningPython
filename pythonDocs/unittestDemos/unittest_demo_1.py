# -*- coding: utf-8 -*-
import unittest
import logging


# 可以在pythonDocs上执行文件夹下继承了TestCase的测试类， python -m unittest discover -s .\pythonDocs\ -p "*.py"

class TestStringMethods(unittest.TestCase):


    def test_upper(self):
        self.assertEqual("foo".upper(),"FOO")
    

    def test_isupper(self):
        self.assertTrue("FOO".isupper())
        self.assertFalse("Foo".isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(),['hello','world'])

        with self.assertRaises(TypeError):
            s.split(2)


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    unittest.main()
        

