# function to add two intergers
def add(num1, num2):
    return num1+num2

print (add(5,10)) #pass to print function

result = add(5,10)
print (result) #assign to a variable

def say_hello():
    print ('Hello There!')

# function that returns the length of a string

def length(string):
    return len(string)

#function to return the sum of integers

def sum_of_intergers(a_list):
    result = 0
    for num in a_list:
        if type(num) is int:
            result=num+result

    return (result)

# function to reverse a string

def rev_string(string):
    idx = len(string) - 1
    result = ''
    while idx >= 0:
        result += string[idx]
        print (idx)
        idx -= 1

    return (result)
print (rev_string('some random string'))

# reverse string in one liner

def one_line_reverse(string):
    return string [::-1]

# using a for loop - danielas soln

def daniela_reverse(string):
    for char in string:
        result = char + result
    return result
print(daniela_reverse ('shilaj'))


'''
val = 1
while val < 10:
    print (val)
    val = val+1 #increment val
'''

