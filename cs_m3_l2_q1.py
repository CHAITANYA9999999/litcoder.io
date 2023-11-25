import sys
def SlidingSubarrayBeauty (nums,k,x):
    ans = []
    for i in range(len(nums) -k+1):
        ans.append(sorted(nums[i:i+k])[x-1])
    return ans
user_input = input()
nums = list(map(int, user_input.split()))
k = int(input())
x = int(input())
output = SlidingSubarrayBeauty (nums,k,x)
for i in output:
    print(i, end=' ')