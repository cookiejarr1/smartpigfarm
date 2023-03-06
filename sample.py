import requests

for i in range(500):
    request = requests.get('http://192.168.0.181/sensorsdata')
    print("UPDATE:", i, request.json())
    print()
