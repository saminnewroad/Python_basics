# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 15:12:30 2020

@author: 18502
"""
def count(list,name):
    count_name=0
    for num in list:
        if num==name:
            count_name=count_name+1
    return count_name

a=['samin', 'reena', 'john', 'samin', 'ram', 'reena', 'samin', 'samin', 'reena', 'john', 'samin', 'ram', 'reena', 'samin']
b=set(a)
for num in b:
    print(num +str(count(a,num)))