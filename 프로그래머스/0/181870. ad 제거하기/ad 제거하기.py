def solution(strArr):
    a = []
    for i in range(len(strArr)):
        if 'ad' not in strArr[i]:
            a.append(strArr[i])
    
    
    return a