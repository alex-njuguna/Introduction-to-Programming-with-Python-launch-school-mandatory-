# method 1
info = 'xyz:*:42:42:Lee Kim:/home/xyz:/bin/zsh'
print(info.replace(':', '+'))

# method 2
def replace_colon(string):
    new_string = ''
    for letter in string:
        if letter == ':':
            new_string += '+'
        else:
            new_string += letter

    print(new_string)

replace_colon(info)

# method 3
parts = info.split(':')
print('+'.join(parts))