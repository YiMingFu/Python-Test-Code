# -*- coding: UTF-8 -*-
import xlrd
import xlwt
import json

workbook = xlrd.open_workbook('/Users/Frozen/Desktop/CRM.xlsx')
tempName = workbook.sheet_names()
print(json.dumps(tempName).decode("unicode-escape"))


sheet2_name = workbook.sheet_names()[0] 
print(json.dumps(sheet2_name).decode("unicode-escape"))


sheet2 = workbook.sheet_by_index(0) # sheet索引从0开始 

rows = sheet2.row_values(0) # 获取第四行内容  
cols = sheet2.col_values(0) # 获取第三列内容  


print(json.dumps(rows).decode("unicode-escape"))
print(json.dumps(cols).decode("unicode-escape"))