def solution(num):
    temp = num
    count = 0
    while temp != 1:
        if temp % 2 == 0:
            temp /= 2
            count += 1
        else: 
            temp = temp * 3 + 1
            count += 1
    return count if count < 500 else -1
