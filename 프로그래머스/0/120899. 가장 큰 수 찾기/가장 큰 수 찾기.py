def solution(array):
    answer = max(array)
    idx = 0
    for i in array:
        if i == answer:
            return [answer, idx]
        idx += 1