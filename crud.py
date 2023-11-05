numbers = [1,2,3,4,5]
print(numbers[1])
numbers[1] = 8
print(numbers)

numbers.append(77);
print(numbers)

numbers.insert(0,9)
print(numbers)

task = [200,300,400]
fusion = numbers + task
print(fusion)

print(fusion.index(200))

fusion.remove(200)
print(fusion)

fusion.pop()
print(fusion)

fusion.reverse()
print(fusion)

fusion.sort()
print(fusion)