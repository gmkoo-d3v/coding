def solution(arr):
    answer = []
    for i in arr:
        temp = i
        while temp:
            answer.append(i)
            temp -=1
            
    return answer