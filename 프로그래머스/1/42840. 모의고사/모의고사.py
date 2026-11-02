def solution(answ):
    answer = [0] * 3
    q = len(answ)
    a = [1, 2, 3, 4, 5]
    b = [2, 1, 2, 3, 2, 4, 2, 5]
    c = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    for i in range(q):
        u = answ[i]
        if u == a[i % len(a)]:
            answer[0] += 1
        if u == b[i % len(b)]:
            answer[1] += 1
        if u == c[i % len(c)]:
            answer[2] += 1

    l = []
    max_score = max(answer)
    for i, score in enumerate(answer):
        if score == max_score:
            l.append(i + 1)
    return l