from collections import deque

def spanner(ls):
    stack = deque()

    stack.append(0)
    print(1, end=" ")

    for i in range(1, len(ls)):
        while len(stack) != 0 and ls[stack[-1]] <= ls[i]:
            stack.pop()
        if len(stack) == 0:
            print(i+1, end = " ")
        else:
            print(i-stack[-1], end=" ")

        stack.append(i)

spanner([15, 10, 8 , 9, 12, 17])