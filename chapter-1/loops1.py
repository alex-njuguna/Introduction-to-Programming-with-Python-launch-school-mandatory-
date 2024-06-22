my_list = [6, 3, 0, 11, 20, 4, 17]

iterator = 0

# print all numbers
# while iterator < len(my_list):
#     print(my_list[iterator])
#     iterator += 1

# print even numbers with while loop
# while iterator < len(my_list):
#     if my_list[iterator] % 2 == 0:
#         print(my_list[iterator])
#     iterator += 1

# print odd numbers with a for loop
for number in my_list:
    if number % 2 != 0:
        print(number)