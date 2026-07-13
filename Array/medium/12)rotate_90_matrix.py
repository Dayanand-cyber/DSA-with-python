"""
Problem Statement: Given an N * N 2D integer matrix, rotate the matrix by 90 degrees clockwise. The rotation must be done in place, meaning the input 2D matrix must be modified directly..
"""

arr=[]
n=int(input('enter the n :'))
for i in range(n):
    l=[]
    for j in range(n):
        l.append(int(input(f"enter the element at ({i},{j}) :")))
    arr.append(l)
    
#brute force
def rotate_90(arr,n):
    temp=[ [0 for j in range(n)] for i in range(n) ]
    for i in range(n):
        for j in range(n):
            temp[j][n-i-1]=arr[i][j]
    arr=temp
    return arr

def rotate_90_op(arr,n):
    
    #transpose
    for i in range(n):
        for j in range(i+1,n):
            temp=arr[i][j]
            arr[i][j]=arr[j][i]
            arr[j][i]=temp
    
    #reverse row
    for i in range(n):
        first=0
        last=n-1
        while(first<last):
            temp=arr[i][first]
            arr[i][first]=arr[i][last]
            arr[i][last]=temp
            first+=1
            last-=1
    
    return arr
    
    

print(rotate_90_op(arr,n))