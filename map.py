numbers = [1,2,3,4]
numbers_v2 = []

for i in numbers:
    numbers_v2.append(i * 2)

numbers_v3 = map(lambda i: i*2,numbers_v2)
numbers_v3 = list(numbers_v3)

print(numbers)
print(numbers_v2)    
print(numbers_v3)