"""
Problem Statement: Given an integer array nums, rotate the array to the left by one.
"""

n=int(input("enter the n :"))
array=[int(input("enter the element :")) for i in range(1,n+1)]

#brute force(optimal)
def rotate(array):
    first_elemet=array[0]
    for i in range(1,len(array)):
        array[i-1]=array[i]
    array[-1]=first_elemet

rotate(array)
print(f"the rotated array:{array}")