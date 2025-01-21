import numpy as np
import pandas
data=pandas.read_csv("Salary_Data.csv")
print(data)
data1=data.iloc[:,:-1].values
print(data1)
data2=data.iloc[:,-1:].values
print(data2)
print(data1*data2)
result = data1*data2
np.savetxt("multiplication.csv",result)

mat1=np.arrey([[2,3,4,5],
               [4,5,6,7],
               [6,8,9,7]])
print(np.sum(mat1))
print(np.transpose(mat1))
print(np.max(mat1))
print(np.min(mat1))
print(np.std(mat1))
print(np.mean(mat1))
print(np.median(mat1))