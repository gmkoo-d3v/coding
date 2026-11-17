def solution(n):
    r = [[0] * n for _ in range(n)]
    
    for i in range(n):
        r[i][i] = 1
    return r