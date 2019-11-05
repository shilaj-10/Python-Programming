countries=['mexico', 'mexico', 'jamaica', 'tahiti', 'USA', 'thailand', 'greece', 'philippines',
'puerto rico', 'jamaica']

destinations = ['Cozumel', 'Cancun', 'Montego Bay', 'Bora Bora', 'Maui', 'Phuket',
'Mykonos', 'Palawan', 'Vieques', 'Negril']

for idx in range(len(destinations)):
    destinations[idx] += ' - ' + countries[idx]
print (destinations)