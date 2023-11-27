def MergeTwoSortedLinkedLists(arr1,arr2):
    arr = arr1 + arr2
    return sorted (arr)

n = int(input())
arr1=[]
for i in range(n):
    x = int(input()) 
    arr1.append(x)

m = int(input())
arr2 = []
for i in range(m):
    x = int(input())
    arr2.append(x)

sorted_array = MergeTwoSortedLinkedLists(arr1,arr2) 
for i in sorted_array:
    print(i)