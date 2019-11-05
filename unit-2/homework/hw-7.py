
import random 

name = input('enter your name (or e to end): ')

messages = ['hello', 'wassup', 'how are you', 'whats hapenning', 'go eat']


while name != 'e':
    pos = random.randint(0, len(messages)-1)
    print (messages[pos])
    name = input('enter your name (or e to end): ')
