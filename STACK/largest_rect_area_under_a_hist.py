from collections import deque

previousSmallerList = []
nextSmallerList = []

def previousSmaller(ls):
    global previousSmallerList

    stack = deque()
    stack.append(0)
    previousSmallerList.append(-1)

    for index, i in enumerate(ls[1:]):
        while len(stack)!=0 and ls[stack[-1]] >= i:
            stack.pop()

        if len(stack) == 0:
            previousSmallerList.append(-1)
        else:
            previousSmallerList.append(stack[-1])
        
        stack.append(index+1)

def nextSmaller(ls):
    stack = deque()
    result = deque()

    global nextSmallerList

    stack.append(len(ls)-1)
    result.append(len(ls))

    for index, i in enumerate(ls[-2::-1]):
        while len(stack) != 0 and ls[stack[-1]] >= i:
            stack.pop()

        if len(stack) == 0:
            result.append(len(ls))
        else:
            result.append(stack[-1])

        stack.append(len(ls) - 2 - index)

    for i in range(len(result)):
        nextSmallerList.append(result.pop())

myList = [11, 3, 4, 4, 1, 5, 7]

previousSmaller(myList)
nextSmaller(myList)

maxArea = 0
for i,j,k in zip(previousSmallerList, myList, nextSmallerList):
    maxArea = max(maxArea, (abs(k-i-2)+1)*j)

print(maxArea)