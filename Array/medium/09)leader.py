"""
Leaders in an Array
"""

n=int(input("enter the n :"))
arr=[int(input("enter the element :")) for i in range (n)]

#brute force
def leader(arr):
    l=[]
    n=len(arr)
    for i in range(n):
        flag=True
        for j in range(i+1,n):
            if arr[i]<arr[j]:
                flag=False
                break
        if flag:l.append(arr[i])
    return l

#optimal
def leader_op(arr):
    n=len(arr)
    l=[]
    max=arr[-1]
    l.append(max)
    for i in range(n-2,-1,-1):
        if arr[i]>max:
            max=arr[i]
            l.append(max)
    return l[::-1]

print(f"the leader elements are {leader_op(arr)}")