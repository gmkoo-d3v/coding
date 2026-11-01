def solution(my_string):
    sentence = {}
    for i in range(65,91,1):
        sentence[chr(i)] = 0
    for j in range(97,123,1):
        sentence[chr(j)] = 0
    
    for i in my_string:
        if i in sentence:
            sentence[i] += 1
            
    return list(sentence.values())