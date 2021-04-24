# -*- coding: utf-8 -*-
"""
Created on Sat Apr 24 12:16:37 2021

@author: tavis
"""

import pandas

# Reading CSV Files with Pandas:
df = pandas.read_csv('F:/WORK/pyWork/AnalyticsEdge_Python/pyData/User_Data.csv')
print(df)

# Writing CSV Files with Pandas:
df.to_csv('F:/WORK/pyWork/AnalyticsEdge_Python/pyData/IIT-B.csv')

# Reading Excel Files with Pandas
df1 = pandas.read_excel('F:/WORK/pyWork/AnalyticsEdge_Python/pyData/User_Data.xlsx')

df1 = pandas.read_excel('User_Data.xlsx')
print(df1)

# Writing Excel Files with Pandas 
df1.to_excel('IIT-B.xlsx')
df2 = pandas.DataFrame(df1)
print (df2)