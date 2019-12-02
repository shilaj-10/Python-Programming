import requests
import json

url = "https://deezerdevs-deezer.p.rapidapi.com/search"

querystring = {"q":"ed sheeran"}

headers = {
    'x-rapidapi-host': "deezerdevs-deezer.p.rapidapi.com",
    'x-rapidapi-key': "a5dc5b1175mshd8e833ee22d31d5p126e70jsnf8d823747244"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

#print(response.text)

data = response.json()
with open('edsheeran.json', 'w') as edsheeran_file:
    edsheeran_file.write(json.dumps(data))