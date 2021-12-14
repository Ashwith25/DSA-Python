def maxArea(ls):
    maxxResult = 0
    for index, i in enumerate(ls):
        count = 1
        for j in ls[:index]:
            if i<=j:
                count+=1
            else:
                break
        for j in ls[index+1:]:
            if i<=j:
                count+=1
            else:
                break
        
        maxxResult = max(maxxResult, (count*i))
                
        
    return maxxResult

def largestRect(ls):
    res = maxArea(ls[0])
    newRow = ls[0]
    for i in range(1, len(ls)):
        for j in range(len(ls[i])):
            if ls[i][j]:
                newRow[j] = newRow[j] + ls[i][j]
            else:
                newRow[j] = 0
                
        res = max(res, maxArea(newRow))

    return res

print(largestRect([[0, 1, 1, 0], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 0, 0]]))

