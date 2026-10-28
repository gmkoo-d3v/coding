def solution(left, right):
   
    countDic = {}
    for i in range(left, right+1):
        templist = []
        
        for j in range(1,i+1):
            if i % j == 0:
                templist.append(j)

        countDic[i]=len(templist)
    
    result = 0
    for i in countDic:
        if countDic[i] % 2 == 0:
            result += int(i)
        else:
            result -= int(i)
    return result
        
    