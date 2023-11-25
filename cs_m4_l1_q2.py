import sys
def ArrayManipulation(queries,n):       
    arr = [0]*(n+1)
    for query in queries:
        for i in range(query[0], query[1]+1): 
            arr[i] += query [2]
    return max(arr)

array_size = int(input()) 
query_count = int(input()) 
queries = []
for i in range(query_count):
    x=input()
    queries.append(list(map(int, x.split())))
    
print(ArrayManipulation(queries,array_size))