"""
Problem Statement: Given an array nums of size n and an integer k, find the length of the longest sub-array that sums to k. If no such sub-array exists, return 0.
"""

n=int(input("enter the n :"))
array=[int(input("enter the element :")) for i in range(1,n+1)]

def longest_sub(array,k):
    n=len(array)
    max=0
    for i in range(n):
        count=1
        sum=array[i]
        for j in range(i+1,n):
            sum=sum+array[j]
            if(sum<k):
                count+=1
            elif(sum>k):
                break;
            elif(sum==k):
                count+=1
                if max<count:
                    max=count
            else:
                pass
    return max

#optimal 
def longest_sub_op(array,k):
    n=len(array)
    left=0
    right=0
    sum=array[0]
    maximum=0
    while(right<n):
        while(left<=right and sum>k):
            sum-=array[left]
            left+=1
        if(sum==k):
            maximum=max(maximum,right-left+1)
        right+=1
        if(right<n):
            sum+=array[right]
        
print(f"the mx count of {longest_sub_op(array,6)}")                
        