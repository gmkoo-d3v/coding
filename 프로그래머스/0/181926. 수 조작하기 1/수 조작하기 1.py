def solution(n, control):
    result = n
    for c in control:
        if c == 'w':
            result += 1
        elif c == 's':
            result -=1
        elif c == 'd':
            result +=10
        elif c == 'a':
            result -=10
    return result