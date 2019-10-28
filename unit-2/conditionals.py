'''
total = 3

# == checks for equality; = assigns variables

if total==15:
    print ('good')
else:
        print ('bad')


total = 23

if total % 2 == 0:
    print ('even')
else:
    print ('odd')

first_name = 'shilaj'

if len (first_name) >= 6:
    print ('good length')
else:
    print ('bad length')

# comparison operators
# ==
# >
# <
# >=
# <=
# !=

# print corresponding letter for a grade
# if score is 80 - 100, print 'A'
# if score is 60 - 79, print 'B'
# if score is 50 - 69, print 'C'
# otherwise, print 'F'
'''
'''
score = 79

if 80<= score <= 100:
    print ('grade A')
elif 60<= score <= 79:
    print ('grade B')
elif 50<= score <= 59:
    print ('grade C')
else:
    print ('FAIL')

'''
# a non empty string is Truthy
if 'hello world':
    print ('yes, its true')
# an empty string is Falsey
if '':
    print ('its true')
else:
    print ('it is false')  

 # any number that is not 0 is truthy

if 13:
    print ('it is true')

# 0 is falsey

if 0:
    print ('it is true')
else:
    print ('it is false')


a = 10
b = -11

if a>0 or b<0:
    print ('good!')

if a>0 and b<0:
    print ('excellent')
   