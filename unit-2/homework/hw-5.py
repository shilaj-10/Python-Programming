
temperature_readings=[25, 18, -5, 11, -3, -15, 8, -18, 6, 13]
temp_neg=[]
temp_pos=[]

for values in (temperature_readings):
    if values < 0:
        temp_neg.append(values)
        count=0
        for num in (temp_neg):
            count = num+count
            average = count/len(temp_neg) 
print('average of negative readings:', average)

for values in (temperature_readings):
    if values > 0:
        temp_pos.append(values)
        count=0
        for num in (temp_pos):
            count = num+count
            average = count/len(temp_pos) 
print('average of positive readings:', average)



