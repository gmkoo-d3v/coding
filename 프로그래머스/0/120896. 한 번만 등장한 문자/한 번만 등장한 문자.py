def solution(s):
    temp = {}
    answer = []
    for i in s:
        temp[i] = temp.get(i,0) + 1
    for j,k in temp.items():
        if k == 1:
            answer.append(j)
    return "".join(sorted(answer))