# -*- coding: utf-8 -*-

# -------------------------------------------------------------------------------
# Name:         read_excel
# Description:  
# Author:       guohuanyang
# Date:         2021/12/24
# Email         guohuanyang@datagrand.com
# -------------------------------------------------------------------------------

import openpyxl


def read(filepath):

    wb = openpyxl.load_workbook(filepath, keep_vba=False, keep_links=False)
    ws = wb.active
    data = []
    for row in ws.iter_rows():
        data.append([x.value for x in row])
    return data


if __name__ == '__main__':
    read('./驻场人员账号信息.xlsx')
