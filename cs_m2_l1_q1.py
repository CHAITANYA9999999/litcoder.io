import sys
def LongestSubstring(inval):
    i=0
    j=1
    longest=1
    current={inval[0]} 
    while j<len(inval):
        if inval[j] not in current:         
            current.add(inval[j])
        else:
            longest = max(longest,j-i) 
            while inval[i]!=inval[j]:
                current.remove(inval[i])
                i+=1
            i+=1
        j+=1
    longest = max(longest,j-i)
    return longest
inputVal = input()
outputVal = doSomething(inputVal)
print (outputVal)