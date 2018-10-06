import json
import urllib

url = "https://finance.yahoo.com/webservice/v1/symbols/allcurrencies/quote?format=json"

try:
    response = urllib.urlopen(url)
    source = response.read()
except error as e:
    print e.code , "error"


data = json.loads(source)

# print(json.dumps(data, indent=2))

usd_rates = dict()

for item in data['list']['resources']:
    name = item['resource']['fields']['name']
    price = item['resource']['fields']['price']
    usd_rates[name] = price

print(50 * float(usd_rates['USD/INR']))

# py3
# import urllib.request, json
# with urllib.request.urlopen("http://maps.googleapis.com/maps/api/geocode/json?address=google") as url:
#     data = json.loads(url.read().decode())
#     print(data)
