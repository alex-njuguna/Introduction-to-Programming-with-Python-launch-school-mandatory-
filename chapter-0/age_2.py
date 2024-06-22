age = int(input('How old are you? '))
print(f'You are {age} years old.')
increment = 0
for i in range(age+10, age+41, 10):
    increment += 10
    print(f'In {increment} years, you will be {i} years old.')