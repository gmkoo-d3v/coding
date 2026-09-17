def solution(my_string, overwrite_string, s):
    answer = my_string[:s] + my_string[s:].replace(my_string[s:s+len(overwrite_string)],overwrite_string)
    return answer