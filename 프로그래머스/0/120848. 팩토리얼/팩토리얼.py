def solution(n):
    i = 1
    factorial = 1
    
    while factorial * (i + 1) <= n:
        i += 1
        factorial *= i
    
    return i