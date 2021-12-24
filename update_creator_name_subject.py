# -*- coding: utf-8 -*-

# -------------------------------------------------------------------------------
# Name:         update_creator_name_subject
# Description:  
# Author:       guohuanyang
# Date:         2021/12/24
# Email         guohuanyang@datagrand.com
# -------------------------------------------------------------------------------
import read_excel

task_id_index = 0
user_id_index = 2
project_index = 3
subject_index = 4


def update_task_by_id(id, creator_id, name):
    return f'update table_parse_task set creator_id={creator_id}, name="{name}" where id={id};'


def update_task_user_relation_by_task_id(task_id, creator_id):
    return f'update bank_flow_task_user_relation set creator_id={creator_id} where task_id={task_id};'


def update_task_subject_by_task_id(task_id, creator_id, subject_name):
    return f'update bank_flow_subject set creator_id={creator_id}, name="{subject_name}" where task_id={task_id};'


def gen_task_sql(update_item_list):
    txt_list = []
    for item in update_item_list:
        try:
            task_id = item[task_id_index]
            user_id = item[user_id_index]
            project_name = item[project_index]
            subject_name = item[subject_index]
            update_task_sql = update_task_by_id(task_id, user_id, project_name)
            update_task_user_relation_sql = update_task_user_relation_by_task_id(task_id, user_id)
            update_task_subject_sql = update_task_subject_by_task_id(task_id, user_id, subject_name)
            update_task = update_task_sql + update_task_user_relation_sql + update_task_subject_sql
            txt_list.append(update_task)
        except Exception as e:
            print(e)
    return txt_list


def gen_sql_file(excel_file, sql_file):
    item_list = read_excel.read(excel_file)
    print(f"new_task条数:{len(item_list)}")
    txt_list = gen_task_sql(item_list)
    print(f"update条数:{len(txt_list)}")
    print(txt_list)
    txt_str = "\n".join(txt_list)
    with open(sql_file, 'w') as f:
        f.write(txt_str)
    print(txt_str)


if __name__ == '__main__':
    gen_sql_file('new.xlsx', 'update_task_creator_name_subject.sql')
    print('done')
