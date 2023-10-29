# ============================== 1 ===============================
colors_lists = ["red", "blue", "yellow"]
print("\n N-1 ")
print(colors_lists)

# ============================== 2 ===============================
random_dict = {"name": "Alex", "age": 25, "city": "Minsk"}
print("\n N-2 ")
print(random_dict["city"])

# ============================== 3 ===============================
text = "Hello, world"
print("\n N-3 ")
print(len(text))

# ============================== 4 ===============================
random_numb = 42
print("\n N-4 ")
print(random_numb ** 2)

# ============================== 5 ===============================
list_to_ten = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("\n N-5 ")
print(sum(list_to_ten))

# ============================== 6 ===============================
dict_abc = {"a": 1, "b": 2, "c": 3}
print("\n N-6 ")
print(dict_abc["a"] * dict_abc["c"])

# ============================== 7 ===============================
text_about_python = "Python это интересный язык программирования"
print("\n N-7 ")
print(text_about_python[:5])

# ============================== 8 ===============================
print("\n N-8 ")
list_of_numbs = [12, 15, 18, 21, 24]
for i in list_of_numbs:
    print(i % 5)

# ============================== 9-10 ===============================
dict_xyz = {"x": 10, "y": 20, "z": 30}
print("\n N9-10 ")
print(dict_xyz["z"] // dict_xyz["x"])

# ============================== 11 ===============================
list_fruits = ["apple", "orange", "banana"]
dict_fruits = {"fruits": list_fruits}
print("\n N-11 ")
print(dict_fruits["fruits"])

# ============================== 12 ===============================
dict_persons = {"name": "Oleg", "age": 25}
dict_all_persons = {"person": dict_persons}
print("\n N-12 ")
print(dict_all_persons["person"]["age"])

# ============================== 13 ===============================
dict_hobbys = {"name": "Oleg", "hobby": "foot"}
dict_all_hobbys = {"person": dict_hobbys}
print("\n N-13 ")
print(dict_all_hobbys["person"]["hobby"])

# ============================== 14 ===============================
dict_scores = {"name": "Oleg", "score": [1, 10, 100]}
print("\n N-14 ")
print(sum(dict_scores["score"]) / len(dict_scores["score"]))

# ============================== 15 ===============================
list_text = ["Hello", {"world": 1, "!": 2}]
print("\n N-15 ")
print(list_text[1]["!"])

# ============================== 16 ===============================
list_elements = [10, "Hello", {"a": 3, "b": 4}]
print("\n N-16 ")
print(list_elements[0] + list_elements[2]["a"])

# ============================== 17 ===============================
list_4elements = [5, "World", {"a": 6, "b": 7}, [8, 9]]
my_dict = {"new" : 223}
list_4elements.append(my_dict)
list_4elements.append(10)
print("\n N-17 ")
print(list_4elements)

# ============================== 18 ===============================
dict_infos = {"name": "oleg",
              "info": {"age": 25, "city": "minsk",
                       "hobbies": ["foot", "volley", "tennis"]}
              }
print("\n N-18 ")
print(dict_infos["info"]["hobbies"])


# ============================== 19 ===============================
dict_friends = {"name": "Oleg",
                "friends":[
                           {"name":"Igor", "age": 20},
                           {"name":"Anton", "age": 25},
                           {"name":"Slava", "age": 30}
                           ]
                }
print("\n N-19 ")
print(dict_friends["friends"][0])

