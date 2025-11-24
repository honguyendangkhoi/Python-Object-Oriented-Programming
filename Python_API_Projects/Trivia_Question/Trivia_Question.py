import json, requests

parameters={
    "amount":10,
    "category":11,
}

respone=requests.get(url="https://opentdb.com/api.php",params=parameters)
respone.raise_for_status()

data=respone.json()
print(data["results"])