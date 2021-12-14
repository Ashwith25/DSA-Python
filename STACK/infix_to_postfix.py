from collections import deque

def isOperand(ele):
    return True if ord('A') <= ord(ele) <= ord('Z') or ord('a') <= ord(ele) <= ord('z') else False

def checkPrecedence(char):
    if char == '+' or char == '-':
        return 1
    elif char == '*' or char == '/':
        return 2
    elif char == '^':
        return 3
    else:
        return -1

def infixToPostfix(expr):
    result = []
    stack = deque()
    for i in expr:
        if i == '(':
            stack.append(i)
        elif i == ')':
            while len(stack) != 0 and stack[-1] != '(':
                result.append(stack.pop())
            stack.pop()
        elif isOperand(i):
            result.append(i)
        else:
            while len(stack) != 0 and checkPrecedence(i) <= checkPrecedence(stack[-1]):
                result.append(stack.pop())
            stack.append(i)
    while len(stack) != 0:
        result.append(stack.pop())

    return result

print(*infixToPostfix("a+b*(c^d-e)^(f+g*h)-i"))