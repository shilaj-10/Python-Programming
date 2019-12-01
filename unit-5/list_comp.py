# list comprehension can be used to create a new list from an existing one

nums = [1,3,6,8,11,15,18]
# create new list with only even numbers - traditional method
even_nums=[]
for num in nums:
    if num % 2 == 0:
        even_nums.append(num)
print (even_nums)

# with list comprehension
new_even_nums = [num for num in nums if num % 2 ==0]
print (new_even_nums)
#[num for num in nums if num % 2 ==0] -> list comprehension approach

# list with the square of the even numbers
even_square=[ val*val for val in nums if val % 2 == 0]
print (even_square)

#creat a list of the titleswith 't' in the names

titles = ['lord of the ring', 'the time machine', 'the great gatsby','moby dick','chronicles of narnia','fast and the furious']
new_titles=[names for names in titles if 't' in names]
print(new_titles)

#convert a string to upercase
string = 'this is a sample sentence'
# creates a list of the characters - upper case
capital = ''.join([char.upper() for char in string ])
print (capital)

# if/else goes before the for
# if number is less than 10, add ten, else subtract 10

vals = [15,12,3,8,-1,7,11,25,0,10]
ten_list = [val + 10 if val < 10 else val - 10 for val in vals]
print(ten_list)

#dictionary comprehension 
person = {'name':'alice', 'job':'engineer','city':'toronto'}
# create a new dictionary that has the first initial of both key and value
# {'n':'a', 'j':'e', 'c':'t'}

new_person={key[0]:value[0] for key, value in person.items()}
print(new_person)

