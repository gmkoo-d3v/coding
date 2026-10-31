def solution(array, height):
    answer = 0
    array = sorted(array)
    for i in array:
        if i > height:
            answer += 1
    return answer