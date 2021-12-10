import requests
from requests.auth import HTTPBasicAuth
import json
response = requests.get("http://api.open-notify.org/astros.json")

print(response.json())


query = {'lat':'45', 'lon':'180'}
response = requests.get('http://api.open-notify.org/iss-pass.json', params=query)
print(response.json())
print(response.headers["date"])
print(response)

#Log into GitHub using BasicAuth
response2 = requests.get('https://api.github.com/user',auth=HTTPBasicAuth('david.ihle@gmail.com', 'Canuck$99'))
print(response2.json())
text = json.dumps(response2.json(), sort_keys=True, indent=4)
print(text)
#Example of good Try/Catch code
try:
    response = requests.get('http://api.open-notify.org/astros.json', timeout=5)
    response.raise_for_status()
    # Code here will only run if the request is successful
except requests.exceptions.HTTPError as errh:
    print(errh)
except requests.exceptions.ConnectionError as errc:
    print(errc)
except requests.exceptions.Timeout as errt:
    print(errt)
except requests.exceptions.RequestException as err:
    print(err)