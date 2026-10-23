def solution(n):
    temp = []
    n = str(n)
    for i in range(len(n)):
        temp.append(n[i])
    answer = sorted(temp, reverse = True)
    answer = int("".join(answer))
    return answer