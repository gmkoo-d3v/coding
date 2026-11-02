from collections import deque

def solution(prices):
    
    
    que = deque(prices)
    count = []

    
    while que:
        timer = 0
        a = que.popleft()
        for i in que:
            timer += 1
            if a > i:
                break
        count.append(timer)        
                
        




    return count