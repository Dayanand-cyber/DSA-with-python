"""
Problem Statement: Given an integer array nums of size n, return the majority element of the array.

The majority element of an array is an element that appears more than n/2 times in the array. The array is guaranteed to have a majority element.
"""

n=int(input("enter the n :"))
arr=[int(input("enter the element :")) for i in range (n)]

#optimal
def majority_elemet(arr):
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

print(f"the majority element is {majority_elemet(arr)}")