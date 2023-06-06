
# next_permutation : find next lexicographically greater permutation

# input = [1,3,2]
# output = [2,1,3]1


def next_permutation(arr):
    temp = -1
    for i in range(len(arr)-2,-1,-1):
        if(arr[i]>arr[i+1]):
            temp = i 
    
    if(temp == -1):
        return arr[::-1]
    
    for i in range(len(arr)-1,-1,-1):
        if(arr[i]< arr[temp]):
            arr[i],arr[temp] = arr[temp],arr[i]
        
    arr[temp+1:] = arr[temp+1:][::-1]
    return arr 

input = [1,3,2]
print(next_permutation(input))