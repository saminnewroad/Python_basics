# -*- coding: utf-8 -*-
"""
Created on Tue Feb  4 16:00:31 2020

@author: 18502
"""

Hour=float(input('Enter Work Hour   :'))
Rate=float(input('Enter Rate   :'))
Regular=0
if Hour<40: Regular=(Hour*Rate) else: Regular=(40*Rate)

print(Regular)