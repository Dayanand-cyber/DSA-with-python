"""
Problem Statement: Given an integer array nums of size n, return the majority element of the array.

The majority element of an array is an element that appears more than n/2 times in the array. The array is guaranteed to have a majority element.
"""

n=int(input("enter the n :"))
arr=[int(input("enter the element :")) for i in range (n)]

#brute force
def majority_element(arr):
    n=len(arr)
    element=-1
    for i in arr:
        count=0
        for j in arr:
            if i==j:
                count+=1
        if count>n//2:
            element=i
    return element

#optimal
def majority_element_op(arr):
    n=len(arr)
    element=arr[0]
    count=1
    for i in range (n):
        if count == 0:
            element=arr[i]

        if arr[i] == element:
            count+=1
        else:
            count-=1
    element_count=0
    for i in arr:
        if i == element:
            element_count+=1
    if element_count>n//2:return element
    else:return None

print(f"the majority element is {majority_element_op(arr)}")