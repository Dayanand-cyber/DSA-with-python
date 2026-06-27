"""
Problem Statement: Given an array of integers arr[] and an integer target.

1st variant: Return YES if there exist two numbers such that their sum is equal to the target. Otherwise, return NO.

2nd variant: Return indices of the two numbers such that their sum is equal to the target. Otherwise, we will return {-1, -1}.
"""

n=int(input("enter the n :"))
arr=[int(input("enter the element :")) for i in range (n)]

#brute force
def two_sum(arr,target):
    n=len(arr)
    for i in range(n):
        for j in range(i+1,n):
            if(arr[i]+arr[j]==target):
                return "yes"
    return "no"
target=int(input("enter the target :"))
print(f"does the array have aleast one pair whos sum is {target} :{two_sum(arr,target)}")