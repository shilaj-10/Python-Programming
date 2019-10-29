# sum of even nums between 1000 - 10000
total = 0
for num in range (1000, 10001):
    if num %2 == 0:
        total = total + num
print (f'the sum of even numbers between 1000 and 10000 is {total}')
