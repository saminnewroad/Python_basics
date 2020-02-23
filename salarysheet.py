# -*- coding: utf-8 -*-
"""
Created on Sun Jan 26 10:52:32 2020

@author: 18502
"""
import pandas as pd
salary_sheet={'name':['samin','reena','siddhant','hari', 'shyam','krishna', 'ricky','saylendra'],
              'base':[35000,30,1,31114,302,3321,3110,314],
              'overtime':[0,50,0,25,70,12,0,0]}
salary_table=pd.DataFrame(salary_sheet)
print(salary_table)


print(salary_table['base'])
print(salary_table['overtime'])
print(salary_table.loc[salary_table['name']=='reena'])
print(salary_table.loc[salary_table['base']>38])

#adding new column based on base and overtime column
salary_table['salary']=salary_table['base']*salary_table['overtime']
print(salary_table)

#adding new row in table
newentry={'name':['ram'],'base':[35],'overtime':[30]}
#new_table=pd.DataFrame(newentry,index=[0])
new_table=pd.DataFrame(newentry)

#concatenate two tables to add the row
salary_table=pd.concat([salary_table,new_table],ignore_index=True)
salary_table['salary']=salary_table['base']*salary_table['overtime']
#sort table by column names
salary_table=salary_table.sort_values(by=['name'])
#reset index after sort
salary_table=salary_table.reset_index()  #'it adds new column name index'
salary_table=salary_table.drop(['index'],axis=1)

salary_table.to_csv('C:/Users/18502/Desktop/test/salary_sheet_data.csv')

asdf=pd.read_csv('C:/Users/18502/Desktop/Pandas-Data-Science-Tasks-master/SalesAnalysis/Sales_Data/Sales_April_2019.csv')