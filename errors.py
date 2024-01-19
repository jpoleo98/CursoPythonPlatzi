"""
age = 10

if age<18:
    raise Exception('QUE PASA MENOR!!!!')"""

try:
    print(0/0)
except Exception as e:
    print(e)