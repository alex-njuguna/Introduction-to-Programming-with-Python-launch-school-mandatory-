def number_range(num):
    if num >= 0 and num <=50:
        print(f'{num} is between 0 and 50')
    elif num > 50 and num <= 100:
        print(f'{num} is between 50 and 100')
    elif num > 100:
        print(f'{num} is greater than 100')
    else:
        print(f'{num} is less than 0')

number_range(0)
number_range(25)
number_range(50)
number_range(75)
number_range(100)
number_range(101)
number_range(-1)
