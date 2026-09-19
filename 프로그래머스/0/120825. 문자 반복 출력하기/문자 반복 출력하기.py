def solution(my_string, n):
    a = []
    
    for char in my_string:
        a.append(char*n)
    return "".join(a)    