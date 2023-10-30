# ============================== 1,1 ===============================
print("\n N-1 ")

import json

with open("city.list.json", "r") as f:
    data = list(json.load(f))

list_of_cities = len(data)
print("Quantity of cities in the list: ", list_of_cities)

# ============================== 2 ===============================
print("\n N-2 ")

cities_in_countries = []
for i in data:
    cities_in_countries.append(i["country"])


key = set(cities_in_countries)
quantity_of_cities = dict.fromkeys(key, 0)
for key in cities_in_countries:
    quantity_of_cities[key] += 1


print(quantity_of_cities)

# ============================== 3 ===============================
print("\n N-3 ")
count = [i for i in data if i["coord"]["lat"] < 0]
#for i in data:
    #if i["coord"]["lat"] < 0:
        #count += 1
print(f"number of cities in the northern hemisphere: {len(count)} ")


