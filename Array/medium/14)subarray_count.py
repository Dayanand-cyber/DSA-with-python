"""
Problem Statement: Given an array of integers and an integer k, return the total number of subarrays whose sum equals k. A subarray is a contiguous non-empty sequence of elements within an array.
"""

n=int(input("enter the n :"))
arr=[int(input("enter the element :")) for i in range (n)]

def subarray_count(arr,k):
    n=len(arr)
    count=0
    for i in range(n):
        sum=0
        for j in range(i,n):
            sum+=arr[j]
            if sum>k:break
            if sum==k:count+=1
    return count
k=int(input("enter the target sum :"))
print(subarray_count(arr,k))