def solution(arr1, arr2):
    temp = []
    for i in range(len(arr1)):
        temp.append([])
        
        for j in range(len(arr1[i])):
            temp[i].append(arr1[i][j] + arr2[i][j])
    return temp