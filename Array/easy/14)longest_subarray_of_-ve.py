"""
Problem Statement: Given an array containing both positive and negative integers, we have to find the length of the longest subarray with the sum of all elements equal to zero.
"""

n=int(input("enter the n :"))
array=[int(input("enter the element :")) for i in range(1,n+1)]

#brute force
def long_sum(array):
    n=len(array)
    length=0
    for i in range(n):
        sum=array[i]
        for j in range(i+1,n):
            sum+=array[j]
            if sum==0:length=max(length,j-i+1)
    return length



print(f"the lenght of longest subarray with sum zero is {long_sum(array)}")