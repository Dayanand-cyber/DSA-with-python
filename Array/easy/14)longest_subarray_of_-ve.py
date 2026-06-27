"""
Problem Statement: Given an array containing both positive and negative integers, we have to find the length of the longest subarray with the sum of all elements equal to zero.
"""

n=int(input("enter the n :"))
array=[int(input("enter the element :")) for i in range(1,n+1)]

def long_sum(array):
    left=0
    right=0
    n=len(array)
    count=0
    max=0
    while(right<n):
        while(left<=right and summ>0):
            left+=1
            sum-=array[left]
        

        if(right<n):
            right+=1
            summ+=array[right]