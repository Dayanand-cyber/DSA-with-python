"""
Problem Statement: Given an array, find the second smallest and second largest element in the array. Print ‘-1’ in the event that either of them doesn’t exist.

"""
n=int(input("enter the n :"))
array=[int(input("enter the element :")) for i in range(1,n+1)]


def second_largest(array):
    if(len(array)<=1):return -1
    
    first_largest=float('-inf')
    second_largest_no=float('-inf')
    
    for i in array:
        if first_largest<i:
            second_largest_no=first_largest
            first_largest=i
        elif  second_largest_no<i:
            second_largest_no=i

    return second_largest_no


def second_smallest(array):
    if(len(array)<=1):return -1
    
    first_smallest=float('inf')
    second_smallest_no=float('inf')
    
    for i in array:
        if first_smallest>i:
            second_smallest_no=first_smallest
            first_smallest=i
        elif second_smallest_no>i:
            second_smallest_no=i
            
    return second_smallest_no
    
print(f"the second largest no in the array is {second_largest(array)}")
print(f"the second smallest no in the array is {second_smallest(array)}")