"""
Problem Statement: Given an integer array sorted in non-decreasing order, remove the duplicates in place such that each unique element appears only once. The relative order of the elements should be kept the same.
"""

n=int(input("enter the n :"))
array=[int(input("enter the element :")) for i in range(1,n+1)]

#brute force apporch
def remove_duplicate(array):
    s=set()
    index=0
    for i in array:
        if i not in s:
            s.add(i)
            array[index]=i
            index+=1
    return index

#optimal
def remove_duplicate_op(array):
    i=0
    for j in range(1,len(array)):
        if array[i]!=array[j]:
            i+=1
            array[i]=array[j]
    return i+1
no_of_unique_element=remove_duplicate_op(array)
print(f"the no of unique elements are {no_of_unique_element}")
print(f"the array is :{array[:no_of_unique_element]}")