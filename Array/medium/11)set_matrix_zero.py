"""
Problem Statement: Given a matrix if an element in the matrix is 0 then you will have to set its entire column and row to 0 and then return the matrix..
"""
arr=[]
row=int(input("enter the no of rows :"))
col=int(input("enter the no of columns :"))
for i in range(row):
    l=[]
    for j in range(col):
        l.append(int(input(f"enter the element at ({i},{j}) :")))
    arr.append(l)
    
#brute force
def set_zero(arr,row,col): 
    for i in range(row):
        for j in range(col):
            if arr[i][j]==0:
                for k in range(row):
                    if arr[k][j]!=arr[i][j]:
                        arr[k][j]=-1
                for k in range(col):
                    if arr[i][k]!=arr[i][j]:
                        arr[i][k]=-1
    for i in range(row):
        for j in range(col):
            if arr[i][j]==-1:
                arr[i][j]=0
    return arr

print(set_zero(arr,row,col))