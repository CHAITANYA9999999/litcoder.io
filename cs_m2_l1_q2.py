import sys
def SimpleTextEditor(command_list):
    commands = command_list.split(',')
    prev_stack=[]
    stack = []
    for command in commands:
        if command[0]=='1':
            prev_stack=stack
            stack.extend(list(command[2:]))
        elif command[0]=='2':
            prev_stack=stack
            stack=stack[:-int(command[2])]
        elif command[0]=='3':
            print(stack[int(command[2])-1])
        else:
            stack = prev_stack

inputVal = input()   
SimpleTextEditor(inputVal)