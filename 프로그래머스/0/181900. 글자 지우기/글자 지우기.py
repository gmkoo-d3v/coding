def solution(my_string, indices):
    answer = ''
    s = sorted(indices)
    
    for i in range(len(my_string)):
        if i not in s:
            answer += my_string[i]
    
    
    return answer