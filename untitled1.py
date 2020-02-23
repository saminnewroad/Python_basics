# -*- coding: utf-8 -*-
"""
Created on Sun Feb 23 09:46:26 2020

@author: 18502
"""
import pandas as pd
x={'b':[2,4],'c':[11,7]}
x=pd.DataFrame(x)
y={'b':[3,6],'c':[2,7]}
y=pd.DataFrame(y)
z={'b':[3,6],'c':[2,7]}
z=pd.DataFrame(z)


x=pd.concat([x,y,z],ignore_index=True)
x.to_csv('C:/Users/18502/Desktop/test/data/5555')
r={'b':[3,6],'c':[2,7]}
r=pd.DataFrame(r)
x=pd.concat([r,x],ignore_index=True)
x.to_csv('C:/Users/18502/Desktop/test/data/5555',index=False)



# =============================================================================
# savetofile(table):
#     table=table.reset_index()  #'it adds new column name index'
#     print(table)
#     table=table.drop(['index'],axis=1)    
#     table.to_csv('C:/Users/18502/Desktop/test/inventory_data.csv',index=False)
# =============================================================================
    



print(x)