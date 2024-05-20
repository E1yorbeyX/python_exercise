# Given two integer numbers, return their product only if the product is equal to or lower than 1000. Otherwise, return their sum.
x = input('insert first number: ')
y = input('insert second number: ')

if x.isdigit() and y.isdigit():
    x = int(x)
    y = int(y)
    if x*y <= 1000:
        print(f'The result is: {x} x {y} = {x*y}')
    else:
        print(f'The result is: {x} + {y} = {x+y}')
else:
    raise TypeError("We allow only integers")