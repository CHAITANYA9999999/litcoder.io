import sys
from queue import LifoQueue 
def doSomething(inval):
    stack1 = LifoQueue()
    stack2 = LifoQueue()
    l = inval.split(',')
    for i in l:
        if i[:2]=='1 ':
            stack1.put(int(i[2:]))
        elif i=='2':
            while stack1.qsize()!=1: 
                stack2.put(stack1.get())
            stack1.get()
            while stack2.qsize():
                stack1.put(stack2.get())
        else:
            stack_copy = list(stack1.queue)
            print(stack_copy)

inputVal = input()
doSomething(inputVal)