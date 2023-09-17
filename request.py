import requests
url = 'http://localhost:5000/api'
r = requests.post(url,json={120, 150})
print(r.json())