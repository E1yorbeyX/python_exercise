#Write a program to iterate the first 10 numbers, and in each iteration, print the sum of the current and previous number.
numberList = list(range(10))
for i in numberList:
    if i != 0 :
        n = i-1
        sum = i + n 
        print(f'Current number {i} previous number {n} sum = {sum}')
    else:
        n = 0
        sum =i+n
        print(f'Current number {i} previous number {n} sum = {sum}')

        
# The version of shown
number_list = list(range(10))
previous = 0

for x in number_list:
    x_sum = x + previous
    print(f'Current number {x} previous number {previous} sum = {x_sum}')
    
    previous = x