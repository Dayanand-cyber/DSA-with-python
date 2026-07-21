"""
Problem Statement: Given a Matrix, print the given matrix in spiral order.
"""


n=int(input("enter the n :"))
arr=[ [int(input(f"enter the ({i},{j}) element ")) for j in range(n)] for i in range (n)]

def sprial_print(arr,n):
    top,bottom,left,right=0,n-1,0,n-1
    ans=[]
    
    while top<=bottom and left<=right:
        for i in range(left,right+1):
            ans.append(arr[top][i])
        top+=1
        for i in range(top,bottom+1):
            ans.append(arr[i][right])
        right-=1
        if(top<=bottom):
            for i in range(right,left-1,-1):
                ans.append(arr[bottom][i])
            bottom-=1
        if(left<=right):
            for i in range(bottom,top-1,-1):
                ans.append(arr[i][left])
            left+=1
    return ans

print(sprial_print(arr,n))