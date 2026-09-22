def solution(n):
    i = 0
    while i != n :
        if 7*(i+1) >= n:
            return i+1
        else:
            i +=1
       