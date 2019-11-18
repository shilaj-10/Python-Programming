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



#problem 1
def reverse_list(lists):
    return lists[::-1]
​#problem 2
def encode_string(string):
    letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    
    results = ""
    for character in string:
        for idx in range(len(letters)):
            if character == letters[idx]:
                results += str(idx + 1)
    return results 
​
​#problem 3
def pivot_split(my_list, my_num):
    left = []
    right = []
    for num in my_list:
        if num < my_num:
            left.append(num)
        else:
            right.append(num)
    return [left, right]



