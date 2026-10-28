def solution(myString):
    temp = list(myString.split("x"))
    answer = []
    for i in temp:
        if len(i) == 0:
            answer.append(0)
        else:
            answer.append(len(i))
    return answer