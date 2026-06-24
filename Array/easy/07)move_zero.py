"""
Problem Statement: You are given an array of integers, your task is to move all the zeros in the array to the end of the array and move non-negative integers to the front by maintaining their order.
"""

n=int(input("enter the n :"))
array=[int(input("enter the element :")) for i in range(1,n+1)]

#brute force(bad time complexity:O(n^2))
def move_zero(array):
    n=len(array)
    i=0
    while(i<n):
        if array[i]==0:
            # time complexity O(n) here 
            array[i+1:n]=array[i+1:n][::-1]
            array[i:n]=array[i:n][::-1]
        i+=1

#optimal
def move_zero_op(array):
    n=len(array)

    j=-1
    for i in range(n):
        if(array[i]==0):
            j=i
            break
    if(j==-1):return

    for i in range (j+1,n):
        if(array[i]!=0):
            array[j],array[i]=array[i],array[j]
            j+=1



move_zero_op(array)
print(array)
    
        