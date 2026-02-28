student_numbers = [i for i in range(1,31)]

for _ in range(28):
    submitted = int(input())
    student_numbers.remove(submitted)
    
print(min(student_numbers))
print(max(student_numbers))