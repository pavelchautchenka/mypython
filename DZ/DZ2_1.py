# ============================== 1 ===============================
firs_number = int(input("введите первое число:"))
second_number = int(input("введите второе число:"))
third_number = int(input("введите третье число:"))
sum_of_three = firs_number+second_number+third_number
print("\n N-1 ")
print(sum_of_three)

# ============================== 2 ===============================
number = int(input("введите ваше число: "))
print("\n N-2 ")
print(f"следующим числом {number} число:", number + 1  )
print(f"Для числа {number} предыдущее число:", number - 1)

# ============================== 3 ===============================
distance_in_cm  = int(input("введите дистанция в см: "))
distance_in_m = distance_in_cm //100
print("\n N-3 ")
print(distance_in_m)

# ============================== 4 ===============================
time_in_min = int(input("введите время в минутах: "))
time_in_hour = time_in_min // 60
print("\n N-4 ")
print(f"{time_in_hour} часов  {time_in_min-time_in_hour*60} минут")

# ============================== 5 ===============================

three_digit_number = int(input("введите трехзначное число: "))
sum_of_three = three_digit_number//100+ three_digit_number % 100 //10 + three_digit_number%10
multiplication_of_three = (three_digit_number//100)* (three_digit_number % 100 //10) * (three_digit_number%10)
print("\n N-5 ")
print(sum_of_three)
print(multiplication_of_three)

# ============================== 6 ===============================

element = int(input("введите ваше число: "))
even_or_odd = element % 2
print("\n N-6 ")
print("четное ?" ,1 > even_or_odd )

# ============================== 7 ===============================
side_of_square = int(input("введите сторону квадрата:"))
print("\n N-7 ")
print("периметр равен: ",side_of_square*4)
print("площадь  равен: ",side_of_square**2)
print("дмагональ квадрата  равна:  ",(side_of_square**2*2)**0.5)

# ============================== 8 ===============================
print("\n N-8 ")
random_list = [1,2,3]
random_list.append("text")
random_list.insert(0,30)
random_list_for_append = [7,8,9]
random_list.append(random_list_for_append)
random_tuple_for_append = (55,56,57)
random_list.insert(2,random_tuple_for_append)
random_list.pop(0)
print(random_list)

