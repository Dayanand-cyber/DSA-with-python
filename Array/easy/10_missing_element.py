"""
Given an array arr[] of size n-1 with distinct integers in the range of [1, n]. This array represents a permutation of the integers from 1 to n with one element missing. Find the missing element in the array.
"""

n=int(input("enter the n :"))
array=[int(input("enter the element :")) for i in range(1,n)]

def missing_element(array):
    n=len(array)
    max_range=n+1
    sum_of_array=sum(array)#O(n)
    sum_of_range=(max_range*(max_range+1))//2
    missing_no=sum_of_range-sum_of_array
    return missing_no


print(f"the missing element is {missing_element(array)}")