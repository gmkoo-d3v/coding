def solution(my_string, m, c):
    temp = len(my_string) // m
    answer = []

    for i in range(temp):
        answer.append(my_string[i * m + (c -1)])
    return ''.join(answer)