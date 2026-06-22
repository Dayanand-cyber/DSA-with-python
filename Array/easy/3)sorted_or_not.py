"""
Problem Statement: Given an array of size n, write a program to check if the given array is sorted in (ascending / Increasing / Non-decreasing) order or not. If the array is sorted then return True, Else return False.
"""

#optimal apporach
n=int(input("enter the n :"))
array=[int(input("enter the element :")) for i in range(1,n+1)]

def sorted_or_not(array):
    if(len(array)==1):return True
    for i in range(1,len(array)):
        if array[i-1]>array[i]:
            return False
    return True

print(f"the array  is not sorted :{sorted_or_not(array)}")