from collections import deque

def solution(arr):
    answer = []
    que = deque(arr)
    
    while que:
        n = que.popleft()
        
        if answer and answer[-1] == n:
            answer.pop()
        else:
            answer.append(n)
    
    
    return answer if answer else [-1]