import pandas as pd
try:
    product=pd.read_csv('C:/Users/18502/Desktop/test/data/00000')
except:
    product={"Name":[],"ID":[],'Price':[],'QTY':[]}
product=pd.DataFrame(product)

Check="y"
while Check=='y':
    
    n=input("Enter Name:   ")
    i=input("Enter ID:   ")
    p=input("Enter Price:   ")
    q=input("Enter QTY:   ")
    addproduct={"Name":[n],"ID":[i],'Price':[p],'QTY':[q]}
    addproduct=pd.DataFrame(addproduct)
    product=pd.concat([product,addproduct],ignore_index=True)
    Check=input("Y to Add Product:   ")
    
# =============================================================================
# product=product.reset_index()
# product=product.drop(['index'],axis=1)
# =============================================================================
product.to_csv('C:/Users/18502/Desktop/test/data/00000',index=False)
print(product)



