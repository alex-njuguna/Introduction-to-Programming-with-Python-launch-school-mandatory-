# method 1
my_list = [
    [1, 3, 6, 11],
    [4, 2, 4],
    [9, 17, 16, 0],
]

new_list = my_list[0] + my_list[1] + my_list[2]
for num in new_list:
    if num % 2 == 0:
        print(num)

# method 2
for nested_list in my_list:
    for number in nested_list:
        if number % 2 == 0:
            print(number)
