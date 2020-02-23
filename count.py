# -*- coding: utf-8 -*-
"""
Created on Sun Jan 19 10:15:08 2020

@author: 18502
"""

fname=['ram','shyam','hari','gita','rita','sita','ram','krishna','ram','sita',
            'rita','sita','mohan','ram','shyam','hari','gita','rita','sita','ram','krishna','ram','sita',
            'rita','sita','mohan','ram','shyam','hari','gita','rita','sita','ram','krishna','ram','sita',
            'rita','sita','mohan','ram','shyam','hari','gita','rita','sita','ram','krishna','ram','sita',
            'rita','sita','mohan','ram','shyam','hari','gita','rita','sita','ram','krishna','ram','sita',
            'rita','sita','mohan','ram','shyam','hari','gita','rita','sita','ram','krishna','ram','sita',
            'rita','sita','mohan','ram','shyam','hari','gita','rita','sita','ram','krishna','ram','sita',
            'rita','sita','mohan','ram','shyam','hari','gita','rita','sita','ram','krishna','ram','sita',
            'rita','sita','mohan']
ram_count=0
hari_count=0
mohan_count=0
for num in fname:
    if num=='ram':
        ram_count=ram_count+1
    elif num=='hari':
        hari_count=hari_count+1
    elif num=='mohan':
        mohan_count=mohan_count+1
        
print (ram_count)
print(hari_count)
print(mohan_count)