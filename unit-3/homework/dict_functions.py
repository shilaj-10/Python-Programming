#problem 1
def frequency_counter(input_str):
    result = {}
    for char in input_str:
        if char in result:
            result[char]=result[char]+1
        else:
            result[char]=1
    return result
print (frequency_counter('kkkkksdhdsfbffs'))

#problem 2
def list_to_dict(name, job, city):
    person = {'name':name, 'job':job, 'city':city}
    return person
person1 = list_to_dict('shilaj', 'engineer', 'auckland')
print (person1)

def list_to_dict(name, job, city):
    person = {'name':name, 'job':job, 'city':city}
    return person
print (list_to_dict('shilaj', 'engineer', 'auckland'))
