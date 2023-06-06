

# Sort an array of 0s, 1s and 2s
# Problem Statement: Given an array consisting of only 0s, 1s, and 2s. Write a program to in-place 
# sort the array without using inbuilt sort functions. ( Expected: Single pass-O(N) and constant space)



nums = [2,0,2,1,1,0]


def swap(arr,i,j):
    arr[i],arr[j]=arr[j],arr[i]

def sort(arr):
    low = 0
    high = len(arr) - 1
    i  = 0
    while i<=high:
        
        if arr[i]==0:
            swap(arr,i,low)
            low+=1
            i+=1
        elif arr[i]==1:
            i+=1
        else:
            swap(arr,i,high)
            high-=1

        



sort(nums)
print(nums)