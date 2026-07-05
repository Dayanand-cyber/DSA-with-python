"""
Problem Statement: Given an integer array nums, find the subarray with the largest sum and return the sum of the elements present in that subarray.
"""

n=int(input("enter the n :"))
arr=[int(input("enter the element :")) for i in range (n)]

#brute force
def max_sum(arr):
    n=len(arr)
    maximun_sum=float('-inf')
    for i in range(n):
        sum=0
        for j in range(i,n):
            sum+=arr[j]
            maximun_sum=max(sum,maximun_sum)
    return maximun_sum

#optimal
def max_sum_op(arr):
    maximun_sum=float('-inf')
    sum=0
    for i in range(len(arr)):
        if sum==0:start=i
        sum+=arr[i]
        if sum>maximun_sum:
            maximun_sum=sum
            ans_start=start
            ans_end=i
        if sum<0:sum=0
    for i in range(ans_start,ans_end+1):
        print(arr[i],end="")
    print("\n")
    return maximun_sum

print(f"the largest sum of a subarray {max_sum_op(arr)}")
