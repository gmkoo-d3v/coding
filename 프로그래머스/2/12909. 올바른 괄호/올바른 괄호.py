from collections import deque

def solution(s):
    que = deque([])
    count = 0
    for idx in range(len(s)):
        que.append(s[idx])

    for i in range(len(s)):
        a = que.popleft() 
        if a == chr(40):
            count += 1
        elif count != 0 and a == chr(41):
            count -= 1
        else: return False
    if count == 0: return True
    else: return False
    