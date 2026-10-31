def solution(order):
    answer = 0
    temp = []
    st = str(order)
    for i in range(len(st)):
        temp.append(st[i])
    for k in temp:
        if int(k) == 0:
            continue
        elif int(k) % 3 == 0:
            answer += 1
    return answer