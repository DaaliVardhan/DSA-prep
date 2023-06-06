# Kadane’s Algorithm : Maximum Subarray Sum in an Array
# Problem Statement: Given an integer array arr, find the contiguous subarray (containing at least one number) which
# has the largest sum and returns its sum and prints the subarray.


arr = [-2,1,-3,4,-1,2,1,-5,4]

def twoSum(arr):

    maxi = max(arr)
    sum = 0
    start = 0
    left = right = -1
    for i in range(len(arr)):

        if sum == 0:
            start = i 

        sum += arr[i] 
        if sum > maxi:
            maxi = sum 
            left = start 
            right = i 
        
        if sum<0:
            sum = 0

    print(arr[left:right+1])
    return maxi 

print(twoSum(arr))