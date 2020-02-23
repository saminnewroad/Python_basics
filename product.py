import pandas as pd
try:product=pd.read_csv('C:/Users/18502/Desktop/test/data/000'),
except:
    product={'name':[],'product_id':[],'price':[],'qty':[]}
product=pd.DataFrame(product)
c='yes'
while c=='yes':
    name=input('product  :')
    product_id=input('product_id  :')
    price=input('price  :')
    qty=input('qty  :')
    addproduct={'name':[name],'product_id':[product_id],'price':[price],'qty':[qty]}
    
    addproduct=pd.DataFrame(addproduct)
    c=input('yes or no  :')
    product=pd.concat([product,addproduct],ignore_index=False)
 
    

print(product)
product.to_csv('C:/Users/18502/Desktop/test/data/000')


    







