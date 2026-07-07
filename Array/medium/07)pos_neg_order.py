"""
Problem Statement: There’s an array ‘A’ of size ‘N’ with an equal number of positive and negative elements. Without altering the relative order of positive and negative elements, you must return an array of alternately positive and negative values.
"""

n=int(input("enter the n :"))
arr=[int(input("enter the element :")) for i in range (n)]

#brute force
def order(arr):
    pos=[]
    neg=[]
    for i in arr:
        if i>0:pos.append(i)
        else:neg.append(i)
    count1=0
    count2=0
    for i in range(len(arr)):
        if i%2==0:
            arr[i]=pos[count1]
            count1+=1
        else:
            arr[i]=neg[count2]
            count2+=1
    return arr

#optimal
def order_op(arr):
    n=len(arr)
    pos=0
    neg=1
    new_arr=[0]*n
    for i in arr:
        if i>0:
            new_arr[pos]=i
            pos+=2
        else:
            new_arr[neg]=i
            neg+=2
    return new_arr
print(order_op(arr))