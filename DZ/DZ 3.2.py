# ============================== 1 ===============================
print("\n N-1 ")
random_list = [1, 7, 10]
summ = 0
a = 0
while len(random_list) > a:
    summ += random_list[a]
    a += 1
print(summ)

# ============================== 2 ===============================
print("\n N-2 ")
text = "напишите программу, которая принимает на вход строку и выводит на экран"
vowels = ["а", "е", "и", "о", "у", "ы", "э", "ю", "я"]
count = 0
a = 0
while len(text) > a:
    if text[a] in vowels:
        count += 1
    a += 1
print(count)

# ============================== 3 ===============================
print("\n N-3 ")
list_of_words = ["напишите", "программу" , "которая", "принимает", "на", "вход", "строку"]
a = 0
max_len = 0
max_word = []
while len(list_of_words) > a:
    if len(list_of_words[a]) >= max_len:
        max_len = len(list_of_words[a])
        max_word.insert(0, list_of_words[a])
    a += 1
print(f"максимальная дина {max_len}, и это  слово  '{max_word[-1]}'")

# ============================== 4 ===============================
print("\n N-4 ")
list_of_numbs = [1,2,3,4,5,6,7,8]
new_list_of_numbs = []
a = 0
while len(list_of_numbs) > a:
    if list_of_numbs[a] % 2 == 0:
        new_list_of_numbs.append(list_of_numbs[a]*2)
    else:
        new_list_of_numbs.append(list_of_numbs[a])
    a += 1
print(new_list_of_numbs)

# ============================== 5 ===============================
print("\n N-5 ")
list_of_numbs = [5, 2, 6, -5, 9, 3, 4]
min_numb = list_of_numbs[0]
a = 0
index = 0
while len(list_of_numbs) > a:
    if list_of_numbs[a] <= min_numb:
        min_numb = list_of_numbs[a]
        index = a
    a += 1

print(f"миннимальное значение '{min_numb}',c индексом: '{index}'")

# ============================== 5 ===============================
print("\n N-5 ")
number_two = int(input("введите номер элемента на отрезке  от 2 до ∞ : "))
text_final =f""""
                 1 / {2**(number_two-1)}
               > 1 / {2**number_two} 
                 1 / {2**(number_two+1)}"""
print(text_final)


# ============================== 6 ===============================
print("\n N-6 ")
text = "Привет, мир!"
temp_list = text.split()[::-1]
final_text = " "
a = 0
while len(temp_list) > a:
    final_text += "".join(temp_list[a])
    a += 1
print(final_text)