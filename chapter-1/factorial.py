# method 1
# def factorial(num):
#     components = [i for i in range(num, 0, -1)]
#     product = 1
#     for component in components:
#         product *= component

#     return product

#method 2
def factorial(n):
    product = 1
    while n > 0:
        product *= n
        n -= 1

    return product

print(factorial(1))   # 1
print(factorial(2))   # 2
print(factorial(3))   # 6
print(factorial(4))   # 24
print(factorial(5))   # 120
print(factorial(6))   # 720
print(factorial(7))   # 5040
print(factorial(8))   # 40320
print(factorial(25))  # 15511210043330985984000000