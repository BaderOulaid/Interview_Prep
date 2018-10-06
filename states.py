import json

with open('states.json') as file:
    data = json.load(file)

data['states'][-1] = {
      "name": "Adam",
      "abbreviation": "ad",
      "area_codes": ["205", "251", "256", "334", "938"]
    }

# in place sorted. sorted(list, lambda, reverse) to return sorted list
data['states'].sort(key=lambda x: x['name'], reverse=True)

for state in data['states']:
    # del state['area_codes']
    # state["name"] += "_test_"
    print state["name"]


with open('new_states.json', 'w') as file:
    json.dump(data, file, indent=2)