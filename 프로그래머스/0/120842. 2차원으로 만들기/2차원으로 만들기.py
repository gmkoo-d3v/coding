from collections import deque

def solution(num_list, n):
    answer = []
    que = deque([])

    for k in num_list:
        que.append(k)

    for i in range(len(num_list) // n):
        answer.append([])

        count = n
        while count != 0:
            answer[i].append(que.popleft())
            count -= 1

    return answer
            