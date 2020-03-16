
import unittest
from unittest_index_demo import app
import json


class LoginTest(unittest.TestCase):
    '''构造单元测试案例'''
    def test_empty_user_password(self):
        #创建进行web请求的客户端，使用flask提供的
        client = app.test_client()
        #利用client客户端模拟发送web请求
        ret = client.post("/login",data={})

        #ret是视图返回的响应对象,data属性是响应体的数据
        resp = ret.data

        #因为login视图返回的是json字符串
        resp = json.loads(resp)

        #拿到数据后进行断言判断
        self.assertIn("code",resp)
        self.assertEqual(resp["code"], 400)

if __name__ == '__main__':
    unittest.main()

