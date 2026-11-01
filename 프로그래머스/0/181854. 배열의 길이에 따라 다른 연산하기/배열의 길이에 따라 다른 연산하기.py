def solution(arr, n):
    answer = arr
    leng = len(arr)
    
    if leng % 2 == 0:
        for i in range(1,leng,2):
            answer[i] += n
        
    else:
        for i in range(0,leng,2):
            answer[i] += n
    
    return answer