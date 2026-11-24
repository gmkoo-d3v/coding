def solution(array, n):
    answer = array[0]
    
    for num in array:
        if abs(num - n) < abs(answer - n):
            answer = num
        elif abs(num - n) == abs(answer - n):
            answer = min(answer, num)
    return answer
            