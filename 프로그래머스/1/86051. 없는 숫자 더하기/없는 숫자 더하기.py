def solution(numbers):
    ns = []
    idx = []
    for i in range(0,10,1):
        idx.append(i)    
        
    for j in idx:
        if j not in numbers:
            ns.append(j)
    return sum(ns)
        
    