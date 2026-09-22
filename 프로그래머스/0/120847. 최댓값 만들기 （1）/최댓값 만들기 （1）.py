def solution(numbers):
    ma = 0
    
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if numbers[i]*numbers[j] > ma and i !=j:
                ma = numbers[i]*numbers[j]
    return ma
        