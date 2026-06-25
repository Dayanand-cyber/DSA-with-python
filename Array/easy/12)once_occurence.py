"""
Problem Statement: Given a non-empty array of integers arr, every element appears twice except for one. Find that single one.
"""

n=int(input("enter the n :"))
array=[int(input("enter the element :")) for i in range(1,n+1)]

#brute force
def once_occuerence(array):
    dict={}
    for i in array:
        if i not in dict:
            dict[i]=1
        else:
            dict[i]=dict[i]+1
    for i in dict:
        if dict[i]==1:
            return i
    return -1

#optimal
def once_occuerence_op(array):
    xor=0
    for i in array:
        xor=xor^i
    return xor

print(f"the value with one occurence is {once_occuerence_op(array)}")

