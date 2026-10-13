def solution(num):
    temp = num
    count = 0
    while temp != 1:
        if count < 500:
            if temp % 2 == 0:
                temp //= 2
            
            else: 
                temp = temp * 3 + 1
            
            count += 1
        else: return -1    
    return count
