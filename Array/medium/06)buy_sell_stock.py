"""
Problem Statement: You are given an array of prices where prices[i] is the price of a given stock on an ith day. You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock. Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
"""

n=int(input("enter the n :"))
arr=[int(input("enter the element :")) for i in range (n)]

#brute force
def max_profit(arr):
    n=len(arr)
    maximum=0
    for i in range(n):
        for j in range(i+1,n):
            dif=arr[j]-arr[i]
            if dif>maximum:
                maximum=dif
                day1=i
                day2=j
    if maximum==0:return 0
    else:
        print(day1,day2)
        return maximum

#optimal
def max_profit_op(arr):
    best_price=arr[0]
    maximum=0
    n=len(arr)
    for i in range(1,n):
        dif=arr[i]-best_price
        maximum=max(maximum,dif)
        if arr[i]<best_price:
            best_price=arr[i]
    if maximum==0:return 0
    else:return maximum
    
print(f"the maximum profit is {max_profit_op(arr)}")