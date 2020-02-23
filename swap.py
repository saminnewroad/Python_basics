def swap(a,b):
    numbers=list()
    temp=a
    a=b
    b=temp
    numbers.append(a)
    numbers.append(b) 
    return numbers

x=100
y=200
afterswap=swap(x,y)
x=afterswap[0]
y=afterswap[1]
print(x)
print(y)
