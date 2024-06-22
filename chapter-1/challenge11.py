my_list = [
  [1, 3, 6, 11],
  [4, 2, 4],
  [9, 17, 16, 0],
]

new_list = []
i = 0
while i < len(my_list):
    new_list += my_list[i]
    i += 1
for num in new_list:
    if num % 2 == 0:
        print(num)
