# -*- coding: utf-8 -*-
"""
Created on Sun Jan 26 09:36:17 2020

@author: 18502
"""
import pandas as pd

tallahassee={"name":["krishna", "samin", "ram", "parkash"], 
      "age":[48,38,28,30],
     "grade":["BBS", "BBS","PHD","PHD" ],
     "address":["lamgung", "kathmandu", "Boudha", "panaut"]}

table1=pd.DataFrame(tallahassee)
print(table1)

# accessing only columns
print (table1['name'])

# accessing only row 
# condition ==>> table1['name']=='ram'
# We will use .loc to locate specific row
#table1.loc[condition]
print(table1.loc[table1['name']==input("name")])
print(table1.loc[table1['age']>38])
