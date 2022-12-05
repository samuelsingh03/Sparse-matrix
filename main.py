#...sparse matrix
import numpy as np
from scipy.sparse import csr_matrix
r,c=int(input("Enter the Row Size: ")),int(input("Enter the Column Size: "))
print("Enter the Values ")
mat=[[int(input())for x in range(c)]for y in range(r)]
print("Dense matrix is:")
for i in range(r):
    for j in range(c):
        print(mat[i][j],end=" ")
    print()
sp=csr_matrix(mat)
print("space matrix is\n",sp)
