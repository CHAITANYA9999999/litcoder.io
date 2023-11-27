def SubarrayProductLessThanK(arr,k):
    count = 0
    for i in range(len(arr)): 
        product=arr[i]
        if product<k:
            count+=1
        for j in range(i+1,len(arr)):
            product*=arr[j]
            if product<k:
                count+=1
            else:
                break
    return count
nums = input()
k = int(input())
arr = list(map(int,nums.split()))
print(SubarrayProductLessThanK(arr,k))