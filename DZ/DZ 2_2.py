# ============================== 1 ===============================
print("\n N-1 ")

number = int(input("введите число от 1 до 20: "))

list=[]
a = 0
b = 1
for item in range(19):
    a, b = b, a + b
    list.append(a)

print(list[number-1])

# ============================== 2 ===============================
# Не уверен что понял правильно задание. Подскажите плиз если что то не так.
print("\n N-2 ")

number_two = int(input("введите номер элемента который выведем из последовательности  от 1 до 20: "))
list_empty = []
for i in range(2,number_two+2):
    list_empty.append(1/i)
print(list_empty)

# ============================== 3-4 ===============================
print("\n N-3-4 ")
A = input("введите координаты точки A через запятую: ")
B = input("введите координаты точки B через запятую: ")
coords_A = A.split(',')
coords_B = B.split(',')
valid_A = [int(item) for item in coords_A]
valid_B = [int(item) for item in coords_B]
d  = ((valid_B[0]-valid_A[0])**2+(valid_B[1]-valid_A[0])**2)**0.5
sin_A = (valid_B[1]-valid_A[1]) / d

print(valid_A, valid_B, d,sin_A)

# ============================== 5 ===============================
print("\n N-5 ")
number_two = int(input("введите номер элемента на отрезке  от 2 до ∞ : "))
text_final =f""""
                 1 / {2**(number_two-1)}
               > 1 / {2**number_two} 
                 1 / {2**(number_two+1)}"""
print(text_final)

# ============================== 5 ===============================
print("\n N-5 ")
number_two = int(input("введите номер элемента на отрезке  от 2 до ∞ : "))

list_temp = []
z = 2
for i in range(-1, number_two+1):
    list_temp.append(z)
    z *= 2
    continue
text_final =f""""
                 1 / {list_temp[-4]}
               > 1 / {list_temp[-3]} 
                 1 / {list_temp[-2]}"""
print(text_final)



