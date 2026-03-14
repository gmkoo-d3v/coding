num = [2,2,2,
       3,3,3,
       4,4,4,
       5,5,5,
       6,6,6,
       7,7,7,7,
       8,8,8,
       9,9,9,9]
word = input()

print(sum(num[ord(c)-ord('A')]+1 for c in word))