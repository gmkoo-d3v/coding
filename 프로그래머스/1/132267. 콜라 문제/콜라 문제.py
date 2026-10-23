def solution(a, b, n):
    temp = 0
    count = 0
    while n >= a:
        temp = n // a
        n = n + temp * b - temp * a
        count += (temp*b)
    return count
        
        