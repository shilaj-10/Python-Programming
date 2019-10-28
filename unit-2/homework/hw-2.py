a = 'full_time'
b = 'part_time'
c = 'contract'

worker_type = a
hours_worked = 50

if worker_type == a:
    if 0< hours_worked <= 40:
        wage = 50 * hours_worked
    elif hours_worked > 40:
        wage = 50 * 40 + (60*(hours_worked-40))
        print ('weekly wage = ',wage)
elif worker_type == b:
    if 0< hours_worked <= 20:
        wage = 65 * hours_worked
    elif hours_worked > 20:
        wage = 65*20 + (70*(hours_worked-20))
        print ('weekly wage = ',wage)
elif worker_type == c:
    wage = hours_worked*120*0.75
    print('weekly wage = ',wage)

