"""
Problem Statement: Given an array nums consisting of only 0, 1, or 2. Sort the array in non-decreasing order. The sorting must be done in-place, without making a copy of the original array.
"""

n=int(input("enter the n :"))
arr=[int(input("enter the element :")) for i in range (n)]

def sorting(array):
    count_zero=0
    count_one=0
    count_two=0
    for i in array:
        if i==0:
            count_zero+=1
        elif i==1:
            count_one+=1
        else:
            count_two+=1
    for i in range(len(array)):
        if 0<=i<count_zero:
            array[i]=0
        elif count_zero<=i<count_zero+count_one:
            array[i]=1
        else:
            array[i]=2

#optimal
def swap(arr,index1,index2):
    arr[index1],arr[index2]=arr[index2],arr[index1]

def sorting_op(array):
    low=0
    mid=0
    high=len(array)-1
    while(mid<high):
        if array[mid]==0:
            swap(array,low,mid)
            low+=1
            mid+=1
        elif array[mid]==1:
            mid+=1
        else:
            swap(array,mid,high)
            high-=1
            mid+=1
sorting_op(arr)
print(arr)