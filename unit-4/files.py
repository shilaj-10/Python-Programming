'''
# how to read a file
#second is what we're opening the file for
# if file not in directory add file path and file name
my_file = open('lines.txt', 'r') 

data = my_file.read()
my_file.close() #close file after using it

print (data)
# how do we write to a file
# if we open for writing it will overwrite with new content
my_file = open('lines.txt', 'w')
my_file.write('please add this new line')
my_file.close()
# if the file dosent exist it will create it
my_file = open ('new_file.txt', 'w')
my_file.write('lines for my new file')
my_file.close()

# to add to the end of the file, use append (a)

my_file = open('new_file.txt', 'a')
my_file.write('new file should have a new line')
my_file.close()

my_file = open('new_file.txt', 'a')
my_file.write('\nnew file should have a new line')
my_file.close()
'''
# we can use with if we dont want to have to close every time
with open('lines.txt', 'r') as my_file:
    data = my_file.read()
print(data)