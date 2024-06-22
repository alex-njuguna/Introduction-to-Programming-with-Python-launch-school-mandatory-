stuff = ('hello', 'world', 'bye', 'now')

stuff = list(stuff)
stuff[2] = 'goodbye'

stuff = tuple(stuff)
print(stuff)

pi = 3.141592
str_pi = str(pi)
print(type(str_pi))

name_country = {
    'Alice': 'USA',
    'Francois': 'Canada',
    'Inti': 'Peru',
    'Monika': 'Germany',
    'Sanyu': 'Uganda',
    'Yoshitaka': 'Japan'
}
print(name_country['Alice'])

text = "It's probably pining for the fjords!"

print(text[21:35].rfind('f'))     # 8
print(text.rfind('f', 21, 35))    # 29
