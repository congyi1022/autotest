# coding:utf-8

import xlrd


class ReadExcel:
    """读取excel文件"""

    def getExcel(self):
        cls = []
        xlsx_path = "../testcase/test.xlsx"
        file = xlrd.open_workbook(filename=xlsx_path)
        sheet_size = len(file.sheets())

        for i in range(sheet_size):
            sheet = file.sheet_by_index(i)

            # 获取sheet内的行数
            nrows = sheet.nrows
            for j in range(nrows):
                if sheet.row_values(j)[0] != 'name':
                    cls.append(sheet.row_values(j))
        return cls