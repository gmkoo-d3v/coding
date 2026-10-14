def solution(hp):
    answer = 0
    left = hp
    temp = 0
    temp2 = 0
    temp3 = 0
    
    temp, left = divmod(left, 5)
    answer += temp
    
    temp2, left = divmod(left, 3)
    answer += temp2
    
    temp3, left = divmod(left, 1)
    answer += temp3
        
    
    return answer