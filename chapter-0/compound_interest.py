# compount interest = principal * (1 + r/1000)**time
PRINCIPAL = 1000
RATE = 5
TIME = 5
compound_interest = PRINCIPAL * ((1 + (RATE/100)) ** TIME)
print(f'{compound_interest:,}')

for i in range(1, 6, 1):
    amount = PRINCIPAL * ((1 + (RATE/100)) ** i)
    print(f'year {i}: {amount:,}')