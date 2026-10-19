def solution(my_strings, parts):
    answer = ''
    for idx, (s,l) in enumerate(parts):
        answer += my_strings[idx][s:l+1]
    
    return answer