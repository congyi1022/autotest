# coding:utf-8
from utils import sendRequest
import unittest


class TestLoginWithDataList(unittest.TestCase):
    testdatas = [
        {"name": "正确的邮箱和密码",
         "email": "licongyi@wecash.net",
         "pw": "123456",
         "code": 200,
         "message": "Logged in successfully"},
        {"name": "正确的邮箱和错误密码",
         "email": "licongyi@wecash.net",
         "pw": "123411",
         "code": 200,
         "message": "Wrong credentials"}
    ]

    def setUp(self):
        self.sl = sendRequest.sendRequest()

    def testRunTests(self):
        for testdata in self.testdatas:
            with self.subTest(msg=testdata["name"]):
                res=self.sl.sendrequest(testdata["email"],testdata["pw"])
                self.assertEqual(testdata["code"], res.status_code)
                self.assertIn(testdata["message"], res.text)
