import sys 
def doSomething(inval): 
    rows = [set() for _ in range(9)]
    columns = [set() for _ in range(9)]
    squares = [[set() for _ in range(3)] for _ in range(3)]
    for i in range(9):
        for j in range(9):
            s=inval[i][j]
            if s=='.':
                continue
            elif s in rows[i] or s in columns[j] or s in squares[i//3][j//3]:
                return 'NO'
            else:

                rows[i].add(s) 
                columns[j].add(s)
                squares[i//3][j//3].add(s)
    return 'YES'

inputVal = eval(input())
outputVal = doSomething(inputVal)
print (outputVal)