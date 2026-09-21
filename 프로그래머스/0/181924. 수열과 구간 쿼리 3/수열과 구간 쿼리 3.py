def solution(arr, queries):
    
    for j, k in queries:
        arr[j], arr[k] = arr[k], arr[j]
    return arr