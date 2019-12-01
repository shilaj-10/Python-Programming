import json

with open('nhl.json', 'r') as nhl_file:
    data = json.load(nhl_file)

print(data.keys())

# how many teams in the nhl

num_of_teams = len(data['teams'])
print(num_of_teams)

# when was the boston bruins started
for team in data['teams']:
    if team['name']=='Boston Bruins':
        print (team['firstYearOfPlay'])


# what is the oldest team in nhl
start_date=[]

for team in data['teams']:
    start_date.append(team['firstYearOfPlay'])

print(min(start_date))

#which are the teams in the eastern conference
count = 0
for team in data['teams']:
    if team['conference']['name'] == 'Eastern':
        count = count + 1
print (count)

est_teams = []
for team in data['teams']:
    if team['conference']['name'] == 'Eastern':
        est_teams = est_teams + 1
print (est_teams)

'''
cars = [{'make':'ggg', 'model':'yyy'}, {'make':'rrr', 'model':'ttt'}]

for car in cars:
    print (car['make'])
'''