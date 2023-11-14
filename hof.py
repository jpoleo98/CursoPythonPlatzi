def increment(x):
    return x + 1

def hof(x,func):
    return x + func(x)

result = hof(5,increment)
print(result)