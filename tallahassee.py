# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 14:32:36 2020

@author: 18502
"""
import pandas as pd
tallahassee={"name":["krishna", "samin", "ram", "parkash"], 
      "age":[48,38,28,30],
     "grade":["BBS", "BBS","PHD","PHD" ],
     "address":["lamgung", "kathmandu", "Boudha", "panaut"],"kids":[2,1,0,0]}

tallahassee=pd.DataFrame(tallahassee)

newentry={'name':['hutendra'],'age':[40],'grade':['MBS'],'address':['kathmandu'],'kids':[3]}
newentry=pd.DataFrame(newentry)
tallahassee=pd.concat([tallahassee,newentry],ignore_index=True)
tallahassee['kidage']=tallahassee['kids']+tallahassee['age']
tallahassee['wife']=0


print(tallahassee)
print(tallahassee[input("colum_name : ")])
print(tallahassee.loc[tallahassee['name']==input('search name  :')])
tallahassee.to_csv('C:/Users/18502/Desktop/test/data/tallahassee')