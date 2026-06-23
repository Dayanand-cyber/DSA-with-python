"""
Problem Statement: Given an array, and an element num the task is to find if num is present in the given array or not. If present print the index of the element or print -1.
"""

n=int(input("enter the n :"))
array=[int(input("enter the element :")) for i in range(1,n+1)]

def linear_search(array,item):
    index=-1
    
    for i in range(len(array)):
        if(array[i]==item):
            index=i
            break
    return index

item=int(input("enter the element to be searched ::"))
print(f"the index of {item} is {linear_search(array,item)}")