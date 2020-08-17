# coding:utf-8
from utils import SendRequest
import unittest
import xlrd
from utils.readExcel import ReadExcel

class testLoginwithExcel(unittest.TestCase):
    dataLists=ReadExcel().get_excel()

    def setUp(self) :
        self.sl = SendRequest.SendRequest()

    def testRunTests(self):
        for testdata in self.dataLists:
            with self.subTest(msg=testdata[0]):
                res = self.sl.sendRequest(testdata[1], testdata[2], int(testdata[3]))
                self.assertEqual(testdata[4], int(res.status_code))
                self.assertIn(testdata[5], res.text)
