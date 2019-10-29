#
sent = 'Python Programming at General Assembly is Awesome!!'

new_sent = ''

for char in (sent):
    if char != ' ' and char != 's' and char != 'm':
        new_sent = new_sent + char
print (new_sent)

