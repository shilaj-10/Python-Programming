#problem 1

def rev_list (lst):
    new_list=[]
    idx = len(lst) - 1
    while idx >=0:
        new_list.append(lst[idx])
        idx=idx-1
    return new_list    
print (rev_list([1,2,3,4,5,6,7]))

#problem 2
alpha = 'abcdefghijklmnopqrstuvwxyz'

def encode_string (letters):
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    pos = []
    for letters in alpha:
        # need to find position of those characters
        pos = letters.index
    return pos
print (encode_string('abc'))


#problem 3


