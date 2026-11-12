def solution(i, j, k):
    answer = 0
    for i in range(i,j+1,1):
        s = str(i)
        for j in range(len(s)):
            
            if str(k) in s[j]:
                          
                answer += 1
            
    return answer