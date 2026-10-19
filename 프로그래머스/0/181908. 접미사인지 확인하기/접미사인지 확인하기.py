def solution(my_string, is_suffix):
    answer = 0
    temp = [my_string[i:] for i in range(len(my_string))]
    if is_suffix in temp:
        return 1
    return answer