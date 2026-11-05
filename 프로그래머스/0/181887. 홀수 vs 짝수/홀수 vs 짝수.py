def solution(num_list):

    tempa = 0
    tempb = 0
    for i in range(len(num_list)):
        if i % 2 == 0:
            tempa += num_list[i]
        if i % 2 != 0:
            tempb += num_list[i]
            
    if tempa > tempb: return tempa
    elif tempa < tempb: return tempb
    elif tempa == tempb: return tempa
    