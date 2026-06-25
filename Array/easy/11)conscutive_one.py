"""
Problem Statement: Given an array that contains only 1 and 0 return the count of maximum consecutive ones in the array..
"""

n=int(input("enter the n :"))
array=[int(input("enter the element :")) for i in range(1,n+1)]

def consecutive_one(array):
    maximum=0
    count=0
    for i in array:
        if i==1:count+=1
        else:count=0
        maximum=max(maximum,count)
    return maximum

print(f"the max no of conscutive 1 is {consecutive_one(array)}")