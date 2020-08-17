# coding:utf-8
from utils import sendRequest
import unittest
import xlrd
from utils.readExcel import ReadExcel

class testLoginwithExcel(unittest.TestCase):
    dataLists=ReadExcel().get_excel()

    def setUp(self) :
        self.sl = sendRequest.sendRequest()

    def testRunTests(self):
        for testdata in self.dataLists:
            with self.subTest(msg=testdata[0]):
                res = self.sl.sendrequest(testdata[1],testdata[2], int(testdata[3]))
                self.assertEqual(testdata[4], int(res.status_code))
                self.assertIn(testdata[5], res.text)
