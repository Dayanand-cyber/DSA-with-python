"""
Problem Statement: Given an array of integers, rotating array of elements by k elements either left or right.
"""

n=int(input("enter the n :"))
array=[int(input("enter the element :")) for i in range(1,n+1)]

def rotate(array,k,dir):
    #time complexity:O(n*k)
    if(dir=='l'):
        for i in range(k):
            first=array[0]
            for i in range(1,len(array)):
                array[i-1]=array[i]
            array[-1]=first
    elif(dir=='r'):
        for i in range(k):
            last=array[-1]
            for i in range(len(array)-1,0,-1):
                array[i]=array[i-1]
            array[0]=last
    else:
        print("wrong choice")

#optimal
def reverse(array,start,end):
    while start<end:
        array[start],array[end]=array[end],array[start]
        start+=1
        end-=1
def rotate_op(array,k,dir):
    n=len(array)
    if(dir=='l'):
        reverse(array,0,k-1)
        reverse(array,k,n-1)
        reverse(array,0,n-1)
    elif(dir=='r'):
        reverse(array,0,n-1)
        reverse(array,0,k-1)
        reverse(array,k,n-1)
    else:
        print("wrong choice")


k=int(input("enter the no of rotation :"))
dir=input("enter the direction (l or r) :")
rotate_op(array,k,dir)
print(f"the array after {k} rotation to {dir}:{array}")