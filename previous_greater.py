from collections import deque

def previousGreater(ls):

    stack = deque()
    stack.append(ls[0])
    print("-", end=" ")

    for i in ls[1:]:
        while len(stack)!=0 and stack[-1] <= i:
            stack.pop()

        if len(stack) == 0:
            print("-", end=" ")
        else:
            print(stack[-1], end=" ")
        
        stack.append(i)

previousGreater([12, 10, 20, 22, 15, 14, 18, 32, 20, 22, 19])