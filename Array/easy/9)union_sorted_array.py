"""
Problem Statement: Given two sorted arrays, arr1, and arr2 of size n and m. Find the union of two sorted arrays.

The union of two arrays can be defined as the common and distinct elements in the two arrays.

NOTE: Elements in the union should be in ascending order.
"""

n=int(input("enter the n :"))
array1=[int(input("enter the element :")) for i in range(1,n+1)]

m=int(input("enter the m :"))
array2=[int(input("enter the element :")) for i in range(1,m+1)]

def union_sort(array1,array2):
    array=[]
    n=len(array1)
    m=len(array2)
    i=0
    j=0
    while(i<n and j<m):
        if(array1[i]<array2[j]):
            if array1[i] not in array:
                array.append(array1[i])
            i+=1
        elif(array1[i]>array2[j] ):
            if  array2[j] not in array:
                array.append(array2[j])
                print(array)
            j+=1
        elif(array1[i]==array2[j]):
            if array1[i] not in array:
                array.append(array1[i])
            i+=1
            j+=1
        else:
            pass
    while(i<n):
        if array1[i] not in array:
            array.append(array1[i])
            print(array)
        i+=1
    while(j<m):
        if  array2[j] not in array:
            array.append(array2[j])
            print(array)
        j+=1
    return array

array3=union_sort(array1,array2)
print(f"the sorted union array is {array3}")