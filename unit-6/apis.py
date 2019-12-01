# use the requests module
import requests
import json
response = requests.get('https://statsapi.web.nhl.com/api/v1/teams')

data = response.json()
#pretty print
#print(json.dumps(data, indent=4))

#print (data.keys())
'''
num_of_teams = len(data['teams'])
print(num_of_teams)

active_teams = len(data['active'])
print(active_teams)
'''
#look at the keays on the teams object - check the type

#print(type(data['teams']))
# look at the first item in this list

#print (data['teams'][0])
#pretty print
#print(json.dumps(data['teams'][0], indent=4))
#save to a file

with open('nhl.json', 'w') as nhl_file:
    nhl_file.write(json.dumps(data))

print('done...')
# now we have the file in the folder.

