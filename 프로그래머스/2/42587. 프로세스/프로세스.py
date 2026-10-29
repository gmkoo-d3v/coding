from collections import deque

def solution(priorities, location):
    x = len(priorities)
    que = deque([])
    idx = deque([])
    count = 0

    for n in range(x):
        idx.append(n)

    for k in range(x):
        que.append(priorities[k])

    while que:
        a, aa = que.popleft(), idx.popleft()

        if que and a < max(que):
            que.append(a)
            idx.append(aa)
        else:
            count += 1

            if aa == location:
                return count

    return count