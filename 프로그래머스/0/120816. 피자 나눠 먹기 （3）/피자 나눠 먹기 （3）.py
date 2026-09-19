def solution(slice, n):
    
    for i in range(1,n+1):
        if slice * i >= n:
            return i