# -*- coding: utf-8 -*-
"""
Created on Sun Jan 19 10:59:26 2020

@author: 18502
"""


def count(namelist,name):
    count_num=0
    for nm in namelist:
        if nm==name:
            count_num=count_num+1
    return count_num

fname=['ram','shyam','hari','gita','rita','sita','ram','krishna','ram','sita',
            'rita','sita','mohan','ram','shyam','hari','gita','rita','sita','ram','krishna','ram','sita',
            'rita','sita','mohan','ram','shyam','hari','gita','rita','sita','ram','krishna','ram','sita',
            'rita','sita','mohan','ram','shyam','hari','gita','rita','sita','ram','krishna','ram','sita',
            'rita','sita','mohan','ram','shyam','hari','gita','rita','sita','ram','krishna','ram','sita',
            'rita','sita','mohan','ram','shyam','hari','gita','rita','sita','ram','krishna','ram','sita',
            'rita','sita','mohan','ram','shyam','hari','gita','rita','sita','ram','krishna','ram','sita',
            'rita','sita','mohan','ram','shyam','hari','gita','rita','sita','ram','krishna','ram','sita',
            'rita','sita','mohan']

ram_count=count(fname,'ram')
print(ram_count)

hari_count=count(fname,'hari')
print(hari_count)
    
input_name=input('Enter name of person to count')
input_name_count=count(fname,input_name)
print(input_name_count)
