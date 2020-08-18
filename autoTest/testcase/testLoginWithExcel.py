# coding:utf-8
from utils import SendRequest
import unittest
import xlrd
from utils.readExcel import ReadExcel

class testLoginwithExcel(unittest.TestCase):
    dataLists=ReadExcel().get_excel()
    print(dataLists)

    def setUp(self) :
        self.sl = SendRequest.SendRequest()

    def testRunTests(self):
        for testdata in self.dataLists:
            with self.subTest(msg=testdata[0]):
                res = self.sl.sendRequest(testdata[1], testdata[2])
                self.assertEqual(testdata[3], int(res.status_code))
                self.assertIn(testdata[4], res.text)
