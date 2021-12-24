# -*- coding: utf-8 -*-

# -------------------------------------------------------------------------------
# Name:         select_user
# Description:  
# Author:       guohuanyang
# Date:         2021/12/24
# Email         guohuanyang@datagrand.com
# -------------------------------------------------------------------------------
from read_excel import read as excel_reader
excel_path = './测试流水历史数据-20211224111055.xlsx'
username_index = 2
project_index = 3
subject_index = 4


def gen_user_sql():
    table_data = excel_reader(excel_path)
    username_list = ['"' + x[username_index] + '"' for x in table_data if x[username_index]]
    username_str = f"({','.join(set(username_list))})"
    get_user_id_sql = f"select id, username from users where username in {username_str};"
    print(get_user_id_sql)
    return get_user_id_sql


if __name__ == '__main__':
    gen_user_sql()
