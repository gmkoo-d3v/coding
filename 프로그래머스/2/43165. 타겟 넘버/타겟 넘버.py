from collections import deque

def solution(numbers, target):
    answer = 0

    graph = deque()
    graph.append((0,0))
    while graph:
        idx, tango = graph.popleft()
        if idx == len(numbers):
            if tango == target:
                answer += 1
            continue
        graph.append((idx+1, tango+numbers[idx]))
        graph.append((idx+1, tango-numbers[idx]))
    return answer
