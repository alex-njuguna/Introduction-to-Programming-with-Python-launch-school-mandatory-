# method 1
my_set = {
    'Fluffy',
    'Butterscotch',
    'Pudding',
    'Cheddar',
    'Cocoa',
}
new_set = {}
for key in my_set:
    if len(key) % 2 != 0:
        new_set[key] = len(key)

print(new_set)

# method 2
result = {name: len(name) 
          for name in my_set 
          if len(name) % 2 != 0}
print(result)
