def solution(arr, divisor):
    answer = []
    temp = sorted(arr)
    
    for i in temp:
        if i % divisor == 0:
            answer.append(i)
    
    if len(answer) == 0:
        return [-1]
    return answer