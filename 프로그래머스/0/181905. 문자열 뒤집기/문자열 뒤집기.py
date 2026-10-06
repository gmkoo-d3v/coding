def solution(my_string, s, e):
    temp = []
    temp = my_string[s:e+1]
    temp = temp[::-1]
    answer = []
    answer.append(my_string[:s])
    answer.append(temp)
    answer.append(my_string[e+1:])
    a = "".join(answer)
    return a