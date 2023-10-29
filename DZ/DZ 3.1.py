# ============================== 1 ===============================
print("\n N-1 ")
salut  = input(" Введите приветствие: ")

if len(salut) <31:
    text = f"""
==============================

{salut.center(30)}

==============================
"""
    print(text)

else:
    text = f"""
==============================

{salut[:30]}

==============================
"""
    print(text)

# ============================== 2 ===============================
print("\n N-2 ")

number_a = int(input(" введите первое число: "))
number_b = int(input(" введите второе число: "))
number_c = int(input(" введите третье число: "))
list_t = [number_a, number_b, number_c]
list_definitive = [i for i in list_t if i >0]

print(" сумма положительных чисел: ", sum(list_definitive))

# ============================== 3 ===============================
print("\n N-3 ")
year = int(input("введите год: "))
if year % 4 == 0 and year % 100 != 0 and year % 400 != 0:
    print("Да")
else:
    print("Нет")

# ============================== 4 ===============================
print("\n N-4 ")
first = input("введите первую клетку в формате буква затем число: ")
second = input("введите вторую клетку в формате буква затем число: ")
if first[0] == second[0] or first[1] == second[1]:
    print("Yes")
else:
    print("No")

