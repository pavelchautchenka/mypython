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

# ============================== 4 ===============================
print("\n N-4 ")

import json

geo = {
    "type": "FeatureCollection",
    "features": [],
}

minsk = dict(type="Feature", id = 1211215, geometry = dict(type = "Point",coordinates = [45,25]), properties = dict( iconCaption = "Minsk",marker_color = "#b51eff"))
grodno = dict(type="Feature", id = 4544554, geometry = dict(type = "Point",coordinates = [75,-58]), properties = dict( iconCaption = "grodno",marker_color = "#b51eff"))
vitebs = dict(type="Feature", id = 4548785, geometry = dict(type = "Point",coordinates = [88,13]), properties = dict( iconCaption = "Vitebsk",marker_color = "#b51eff"))
Mogilev = dict(type="Feature", id = 4545445, geometry = dict(type = "Point",coordinates = [12,511]), properties = dict( iconCaption = "Mogilev",marker_color = "#b51eff"))

list_of_citites = [minsk,grodno,vitebs,Mogilev]

for i in list_of_citites:
    geo["features"].append(i)


json_geo = json.dumps(geo,ensure_ascii=False)

with open("geo.json", "w", encoding="utf-8") as json_file:
    json_file.write(json_geo)
