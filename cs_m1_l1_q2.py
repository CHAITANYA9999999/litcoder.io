import sys
def doSomething(inval):
    outval=0
    l=inval.split('')
    inval=[int(x) for x in 1]
    for i in range(len(inval)-1): 
        if inval[i]:
            onecount=1
            zerocount=0
        else:
            onecount=0
            zerocount=1
    for j in range(i+1,len(inval)):
        if inval[j]:
            onecount+=1
        else:
            zerocount+=1
        if onecount==zerocount:
            outval=max(outval,onecount*2)
    return outval
inputVal = input()
outputVal = doSomething(inputVal)
print (outputVal)