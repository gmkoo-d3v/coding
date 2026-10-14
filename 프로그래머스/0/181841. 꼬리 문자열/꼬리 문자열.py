def solution(str_list, ex):
    temp = []
    for i in str_list:
        if ex not in i:        
            temp.append(i)
            
    return "".join(temp)