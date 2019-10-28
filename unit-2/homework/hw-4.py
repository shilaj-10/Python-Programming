sent = 'Python Programming at General Assembly is Awesome'

new_sent = list(sent)

for char in (sent):
    if char == ' ' or char == 's' or char == 'm':
        new_sent.pop(char)
        sent = ''.join(new_sent)
        print (sent)

