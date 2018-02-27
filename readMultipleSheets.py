# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 16:34:44 2018

@author: Aakash Sinha
"""

import pandas as pd

df = pd.read_excel('Schema_POData.xlsx')
# This will read the first sheet into df

xls = pd.ExcelFile('Schema_POData.xlsx')
# This will parse the excel sheet and it is useful when we are reading dataframes in loop

xls.sheet_names
# This will display all the sheet names present in the Excel Sheet

df = pd.read_excel('Schema_POData.xlsx', sheetname="POData")
# This will read sheet "POData" from the excel file

sheet_to_df_map = {}
for sheet_name in xls.sheet_names:
    sheet_to_df_map[sheet_name] = xls.parse(sheet_name)
# This will read all the sheets to a map
