def solution(num_list):
    result = num_list
    if result[-2] < result[-1]:
        result.append(result[-1]-result[-2])
    else:
        result.append(result[-1]*2)
    return result