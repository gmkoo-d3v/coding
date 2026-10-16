def solution(s):
    temp = len(s) // 2
    
    if len(s) % 2 == 0:
        return s[temp - 1: temp + 1]
    else:
        return s[temp]
    