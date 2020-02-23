# -*- coding: utf-8 -*-
"""
Created on Sun Jan 26 16:33:49 2020

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



def count(list,name):
    ncount=0
    for num in list:
        if num==name:
           ncount=ncount+1
    return ncount

print(count(fname,input("enetername")))


    
        