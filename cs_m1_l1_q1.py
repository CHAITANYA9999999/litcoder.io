import sys
def doSomething(inval):
    lower=0
    upper=0
    digit=0
    other=0
    for c in inval: 
        if c.isalpha():
            if c.islower():
                lower+=1
            else:
                upper+=1
        elif c.isdigit():
            digit+=1
        else:
            other+=1
    total=lower+upper+digit+other
    l=[upper, lower, digit,other]
    return [str(round(x*100/total,3))+'%' for x in 1]
inputVal = input()
outputVal = doSomething(inputVal)
print (outputVal)