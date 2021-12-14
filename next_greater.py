from collections import deque

def nextGreater(ls):
    stack = deque()
    result = deque()

    stack.append(ls[-1])
    result.append("-")

    for i in ls[-1::-1]:
        while len(stack) != 0 and stack[-1] <= i:
            stack.pop()

        if len(stack) == 0:
            result.append("-")
        else:
            result.append(stack[-1])

        stack.append(i)

    for i in range(len(result)):
        print(result.pop(), end=" ")

nextGreater([30, 50, 20, 15, 25])