# coding:utf-8
from utils import SendRequest
import unittest

class TestLogin(unittest.TestCase):
    url="http://127.0.0.1:5000/login"


    def setUp(self):
        self.sl= SendRequest.SendRequest()

    def testRightEmailandRightPW(self):
        res=self.sl.sendRequest(self.url, "licongyi@wecash.net", "123456")
        self.assertEqual(200,res.status_code)
        print(res.text)
        self.assertIn("Logged in successfully",res.text)

    def testRightEmailandErrorPW(self):
        res = self.sl.sendRequest(self.url, "licongyi@wecash.net", "111111")
        self.assertEqual(200, res.status_code)
        print(res.text)
        self.assertIn("Wrong credentials", res.text)
if __name__=="__main__":
    unittest.main()



