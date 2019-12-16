import requests
import json

url = "https://api-nba-v1.p.rapidapi.com/seasons/"

headers = {
    'x-rapidapi-host': "api-nba-v1.p.rapidapi.com",
    'x-rapidapi-key': "a5dc5b1175mshd8e833ee22d31d5p126e70jsnf8d823747244"
    }

response = requests.request("GET", url, headers=headers)

#print(response.text)

data = response.json()
with open('nba_seasons.json', 'w') as nba_season_file:
    nba_season_file.write(json.dumps(data))