import json
# https://stackoverflow.com/questions/2352181/how-to-use-a-dot-to-access-members-of-dictionary
jsonData = '{"coord":{"lon":-0.13,"lat":51.51},"weather":[{"id":701,"main":"Mist","description":"mist","icon":"50n"},{"id":500,"main":"Rain","description":"light rain","icon":"10n"}],"base":"stations","main":{"temp":272.14,"pressure":1016,"humidity":74,"temp_min":269.15,"temp_max":275.15},"visibility":10000,"wind":{"speed":2.6,"deg":230},"clouds":{"all":36},"dt":1456379732,"sys":{"type":1,"id":5091,"message":0.0172,"country":"GB","sunrise":1456383302,"sunset":1456421582},"id":2643743,"name":"London","cod":200}';

object = json.loads(jsonData)

# print object["coord"]

weather = object["weather"]
# print weather
# print weather[0]["id"]


# to_stringify = {
#                 "name": "adam", "last": "rose"
# }
#
# print json.dumps(to_stringify)

# with open('data.json') as f:
#     data = json.load(f)
x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

# print(json.dumps(x, indent=4, sort_keys=True))