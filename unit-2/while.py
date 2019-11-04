# while loop is executed only when a certain condition is met
import random # random number module. must always go to the top of the file if using import statement
val = 1
while val < 10:
    print (val)
    val = val+1 #increment val

# guessing game
# all keyword input is string
#correct_answer = 7

correct_answer = random.randint(1,10)

guess = int(input('guess my number(1 - 10)'))

while guess!= correct_answer:
    guess = int(input ('wrong. try again'))

print('youre correct!!')

# how to break a loop? use break

names = ['jack', 'jill','mary','jane','kate']
idx = 0 
while idx< len(names):
    if 'mary' == names[idx]:
        print ('found mary!!')
        break 
    idx = 1+idx 

# how do we loop forever
while True:
    answer = input('continue(y/n)' )
    if answer == 'n':
        break


