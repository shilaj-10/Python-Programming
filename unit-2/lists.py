cohort_4 = ['shilaj','daniela','julian','emma','kyle','chizea','sahil','lizhi','keethri','allaina','christina']

print (len(cohort_4))
#access item in list using position (index)

print (cohort_4[0]) # prints first item in the list


#add items to the list, use append
# . means its a method - append is a list method - this adds to the end of the list
cohort_4.append('princeton')

print (cohort_4)

#remove from the list, use remove
# if duplicates it wont remove all just the first one python finds
cohort_4.remove('julian')
print (cohort_4)

# creat new list with only floats
values = [2.3,45,11,-5,3.5,7.9,11.7,40,85.6,77.1]

float_values = []

for x in values:
    if type (x) is float:
        float_values.append(x)
print (float_values)
