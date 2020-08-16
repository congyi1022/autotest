# coding:utf-8
from utils import sendRequest
import unittest

class TestLogin(unittest.TestCase):
    def setUp(self):
        self.sl= sendRequest.sendRequest()

    def testErrorEmailandErrorPW(self):
        res=self.sl.sendrequest("licongyi@wecash.net","123456")
        self.assertEqual(200,res.status_code)
        print(res.text)
        self.assertIn("Logged in successfully",res.text)

