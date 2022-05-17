# -*- coding: utf-8 -*-

# -------------------------------------------------------------------------------
# Name:         gen_new_excel
# Description:  
# Author:       guohuanyang
# Date:         2021/12/24
# Email         guohuanyang@datagrand.com
# -------------------------------------------------------------------------------
import openpyxl
import read_excel


username_index = 2


def create(data_list, filepath):
    wb = openpyxl.Workbook()
    ws = wb.active
    for row in data_list:
        ws.append(row)
    wb.save(filepath)


def read_txt(txt_file):
    with open(txt_file, 'r', encoding='utf-8') as f:
        data = f.readlines()
    return data


def gen_dict(txt_data):
    txt_data = [x for x in txt_data if x]
    name_dict = {}
    for id_name in txt_data:
        id_name = id_name.replace(" ", "")
        _, id, name, _ = id_name.split(r'|')
        name_dict[name] = int(id)
    print(name_dict)
    return name_dict


def update_data(filepath, txt_file):
    data_list = read_excel.read(filepath)
    print(f"task条数:{len(data_list)}")
    txt_data = read_txt(txt_file)
    name_dict = gen_dict(txt_data)
    new_data_list = []
    error_list = []
    for row in data_list:
        try:
            username = row[username_index]
            user_id = name_dict[username]
            row[username_index] = int(user_id)
            new_data_list.append(row)
        except Exception as e:
            error_list.append(row[2])
            # print(row)
            # print(e)
    print(set(error_list))
    create(new_data_list, 'new.xlsx')


if __name__ == '__main__':
    update_data('流水历史-生产.xlsx', '222.txt')
