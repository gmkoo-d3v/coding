def solution(num_list):
    count = 0
    for i in num_list:
        if min(num_list) > 0: return -1
        if i < 0:
            return count
        else: count +=1
            