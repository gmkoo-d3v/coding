from collections import deque

def solution(array):
    answer = 0
    que = deque(array)
    
    while que:
        i = que.popleft()
        
        while i > 0:
            if i % 10 == 7:
                answer += 1
            
            i //= 10
        
    return answer