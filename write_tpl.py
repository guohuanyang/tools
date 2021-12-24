# -*- coding: utf-8 -*-

# -------------------------------------------------------------------------------
# Name:         write_tpl
# Description:  
# Author:       guohuanyang
# Date:         2021/12/15
# Email         guohuanyang@datagrand.com
# -------------------------------------------------------------------------------
from docxtpl import DocxTemplate
from collections import namedtuple


doc = DocxTemplate('XX私募证券投资基金基金合同补充协议【补充协议模板】.docx')

number = 1
source_fund_name = 'test'
source_fund_admin = 'ghy'
target_fund_name = 'test'
target_fund_admin = 'ghy'

chapter = {
    1: "第一节",
    2: "第二节",
    3: "第三节",
}
first_line = ''
if source_fund_name != target_fund_name:
    first_line = f"{number}.本基金名称/管理人名称从{source_fund_name}变更为{target_fund_admin} \n"
    number += 1
DiffItem = namedtuple("DiffItem", ['source_text', 'target_text'])
test_diff_item = DiffItem(
    source_text="原文原文原文原文原文原文原文原文原文原原文原文原文原文原文原文文原文原文原文原文原文原文文原文原文原文原文",
    target_text='比较文比较文比较文比较文比较文比较文比较文比较文比较文比较文比较文比较文比较文比较文比较文')
test_data = {
    1:      {
            "delete": [test_diff_item, ],
            "replace": [test_diff_item, ],
            "insert": [test_diff_item, ],
            },
    3: {
        "delete": [test_diff_item, ],
        "replace": [test_diff_item, ],
        "insert": [test_diff_item, ],
    },
    2: {
        "delete": [test_diff_item, ],
        "replace": [test_diff_item, ],
        "insert": [test_diff_item, ],
    }
}
sorted_test_data = sorted(test_data.items())

chapter_word = ""
for number, diff_item_dict in sorted_test_data:
    chapter_title = chapter[number]
    tab_space = '   '
    for diff_type in diff_item_dict:
        diff_item_list = diff_item_dict[diff_type]
        if diff_type == 'delete':
            for i, diff_item in enumerate(diff_item_list):
                chapter_word += f'{tab_space}{number}、在“{chapter_title}”章节删除以下内容：\n'
                number += 1
                chapter_word += f'{tab_space}{diff_item.source_text}\n'
        elif diff_type == 'insert':
            for i, diff_item in enumerate(diff_item_list):
                chapter_word += f'{tab_space}{number}、在“{chapter_title}”章节新增以下内容：\n'
                number += 1
                chapter_word += f'{tab_space}{diff_item.target_text}\n'
        else:
            for i, diff_item in enumerate(diff_item_list):
                chapter_word += f'{tab_space}{number}、修改“{chapter_title}”章节的以下内容：\n'
                number += 1
                chapter_word += f"{tab_space}原合同表述为：\n"
                chapter_word += f'{tab_space}{diff_item.source_text}\n'
                chapter_word += f'{tab_space}修改后表述为：\n'
                chapter_word += f'{tab_space}{diff_item.target_text}\n'
context = {
    "fund_name": "test",
    "fund_admin": "ghy",
    "edit_content": chapter_word
}
print(context)
doc.render(context)


doc.save("tmp.docx")
