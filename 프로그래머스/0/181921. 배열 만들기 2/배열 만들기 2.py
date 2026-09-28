def solution(l, r):
    answer = []
    
    def dfs(num):
        if num > r:
            return
        
        if num >= l:
            answer.append(num)
            
        dfs(num * 10)
        dfs(num * 10 + 5)
    dfs(5)
    
    return sorted(answer) if answer else [-1]