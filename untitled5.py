import pandas as pd
try:
    mt=pd.read_csv("C:/Users/18502/Desktop/test/data/o")
except:    
    mt={'item':[],"id":[],"price":[],'qty':[]}
mt=pd.DataFrame(mt)

c="yes"
while c=="yes":
    item=input('I')
    id=input('id')
    price=input('P')
    qty=input('q')
    p={'item':[item],"id":[id],"price":[price],'qty':[qty]}
    p=pd.DataFrame(p)
    c=input("Y/N")
    mt=pd.concat([mt,p],ignore_index=True)
mt=mt.reset_index()
mt=mt.drop(['index'],axis=1)
mt.to_csv("C:/Users/18502/Desktop/test/data/o",index=False)
print(mt)


