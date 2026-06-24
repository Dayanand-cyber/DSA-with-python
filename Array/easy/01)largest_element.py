"""
Problem Statement: Given an array, we have to find the largest element in the array.

"""

n=int(input("enter the n :"))
array=[int(input("enter the element :")) for i in range(1,n+1)]

# brute force(optimal solution)
def largest_element(array):
    largest=0
    for i in array:
        if largest<i:
            largest=i
    return largest
print(f"the largest number in the array is {largest_element(array)}")