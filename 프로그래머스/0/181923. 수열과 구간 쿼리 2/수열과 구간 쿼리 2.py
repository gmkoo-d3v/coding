def solution(arr, queries):
    result = []
    
    for s, e, k in queries:
        candidate = []
        
        for i in range(s,e+1):
            if arr[i] > k:
                candidate.append(arr[i])
                
        if candidate:
            result.append(min(candidate))
            
        else:
            result.append(-1)
            
    return result