def smallest_subarray(arr,target):
    left=0
    current_sum=0
    min_length=float('inf')
    for right in range(len(arr)):
        current_sum+=arr[right]
        while current_sum>target:
            min_length=min(min_length,right-left+1)
            current_sum-=arr[left]
            left+=1
    if min_length==float('inf'):
        return -1
    return min_length
arr=[2,1,5,2,3,2]
target=7
print("Smallest Subarray Length:",smallest_subarray(arr,target))