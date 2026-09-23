def solution(array, commands):
    temp = array
    b = []
    a = []

    for c_index in range(len(commands)):
        i,j,k = commands[c_index]
        b = sorted(temp[i-1:j])
        a.append(b[k-1])
    return a