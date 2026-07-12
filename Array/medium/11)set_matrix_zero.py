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

#optimal
def set_zero_op(arr,row,col):
    first_col=False
    for i in range(row):
        for j in range(col):
            if arr[i][j]==0:
                arr[i][0]=0
                if j==0:
                    if not first_col:first_col=True
                else:
                    arr[0][j]=0
    for i in range(1,row):
        for j in range(1,col):
            if arr[i][0]==0 or arr[0][j]==0:
                arr[i][j]=0
    if arr[0][0]==0:
        for j in range(col):
            arr[0][j]=0
    if first_col:
        for i in range(row):
            arr[i][0]=0    
    return arr        


print(set_zero_op(arr,row,col))