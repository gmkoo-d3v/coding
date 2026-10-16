def solution(n):
    temp = 0
    
    for i in range(1, n+1, 1):
        for j in range(1, n+1, 1):
            if i * j == n:
                temp += j
    return temp