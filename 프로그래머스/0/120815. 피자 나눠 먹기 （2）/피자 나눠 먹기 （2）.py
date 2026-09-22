def solution(n):
    i = 0
    
    while i != n:
        a = 6 * (i +1)
        if a >= n and a % n == 0:
            return i + 1
        else:
            i += 1