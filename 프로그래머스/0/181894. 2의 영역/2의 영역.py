def solution(arr):

    idxs = 0
    idxe = 0
    if 2 not in arr: return [-1]

    for i in range(len(arr)):
        if arr[i] == 2:
            idxs += i
            break
    
    for j in range(len(arr)-1, -1,-1):
        if arr[j] == 2:
            idxe += j
            break
    return arr[idxs:idxe+1]