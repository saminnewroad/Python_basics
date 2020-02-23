# -*- coding: utf-8 -*-
"""
Created on Sun Jan 19 12:24:52 2020

@author: 18502
"""
a=1
b=2
print('sum'+str(a+b))

a=[3,6,8,9,2,5]
min=a[0]
for num in a:
    if min>num: min =num
print('min'+ str(min))

for num in a:
    if num<7:
        print('filter'+str(num))
        
b=input("enter number for + or -:   ")
if int(b)<0:
    print("-ve")
elif int(b)==0: print(0)
else: print('+ve')

c=input("enter number for ODD or Even:  ")
if int(c)%2==0:
    print ('even')
else: print("Odd")

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
for num in fname:
    if num=="ram":
        ram_count=ram_count+1
print('ram_count'+str(ram_count))

def count(list,name):
    name_count=0
    for num in list:
        if num==name:
            name_count=name_count+1
    return(name_count)
    
print('shyam_count'+str(count(fname,"shyam")))

print(count(fname,input("enter name for count:    ")))

d=set(fname)
print(d)
for num in d:
    print(num+str(count(fname,num)))


x=100
y=500
temp=x
x=y
y=temp
print('X-'+ str(x))

print('Y-'+str(y))    
    
d=('samin')
print(d)


sum=0
for num in a:
    sum=sum+num
print('Tota-' + str(sum))