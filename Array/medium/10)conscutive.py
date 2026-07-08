"""
Problem Statement: Given an array nums of n integers.

Return the length of the longest sequence of consecutive integers. The integers in this sequence can appear in any order.
"""

n=int(input("enter the n :"))
arr=[int(input("enter the element :")) for i in range (n)]

#brute force
def linear_search(arr,x):
    for i in arr:
        if i==x:return True
    return False

def conscutive_order(arr):
    longest=0
    
    for i in arr:
        x=i
        count=1
        while linear_search(arr,x+1):
            count+=1
            x+=1
        longest=max(longest,count)
    return longest

print(conscutive_order(arr))