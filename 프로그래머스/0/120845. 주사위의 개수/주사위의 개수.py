def solution(box, n):
    a, b, c = box
    a //= n
    b //= n
    c //= n
    total = a * b * c
    
    return total