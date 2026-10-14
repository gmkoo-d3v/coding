def solution(num_list):
    length = len(num_list)
    total = sum(num_list)
    mul = 1
    if length >= 11:
       
        return total
    if length <= 10:
        for i in num_list:
            mul = mul * i
    return mul
            