def solution(my_string, is_prefix):
    answer = 0
    temp = [my_string[:i] for i in range(1,len(my_string))]
    if is_prefix in temp:
        return 1
    return answer