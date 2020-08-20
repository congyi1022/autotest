# coding:utf-8
from utils import SendRequest
import unittest
from utils.readExcel import ReadExcel
from utils import getTokenAndCookie
import json


class testLoginwithExcel(unittest.TestCase):
    dataLists = ReadExcel().get_excel()

    def setUp(self):
        self.sl = SendRequest.RunMain()

    def testRunTests(self):
        for testdata in self.dataLists:
            name = testdata[0]
            url = testdata[1]
            postdata = testdata[2]
            status_code = testdata[3]
            status_message = testdata[4]
            method = testdata[5]

            datas = getTokenAndCookie.getToken(url)
            crsf_token = datas["token"]
            post_data = json.loads(postdata)
            post_data["csrf_token"] = crsf_token
            cookies = datas["cookie"]

            with self.subTest(msg=name):
                res = self.sl.main_request(method, url, post_data, cookies)
                self.assertEqual(status_code, int(res.status_code))
                self.assertIn(status_message, res.text)
