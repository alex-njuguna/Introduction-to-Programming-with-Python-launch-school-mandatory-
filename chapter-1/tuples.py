tuple_1 = (1, 2, 3, 4, 5)
list_from_tuple_1 = list(tuple_1)
list_from_tuple_1.pop()
list_from_tuple_1.reverse()
list_from_tuple_1.pop()
tuple_2 = tuple(list_from_tuple_1)
print(tuple_2)

my_tuple = (1, 2, 3, 4, 5)
result = my_tuple[3:0:-1]
print(result)