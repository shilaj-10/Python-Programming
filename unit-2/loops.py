# the for loop
name = 'shilaj'
# 
'''
for count in range (1, 11):
    print (name)

for count in range (0, 10):
    print ('shilaj')
'''
'''
for num in range (1, 11):
    if num % 2 == 1:
        print (num)
'''
'''
total = 0

for num in range (1, 11):
    if num % 2 == 0:
        total = num + total  # total += num
print (total)
'''

name = 'shilaj shah'

for alphas in (name):
    if alphas == 'a' or alphas == 'e' or alphas == 'i' or alphas == 'o' or alphas == 'u':
        print (alphas)

my_numbers = [3, 5, 17, 11, 21, 53, -10, -27, 45, 80]

small = my_numbers[0]

for num in my_numbers:
    if num < small:
        small = num
print (small)

