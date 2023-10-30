# ============================== 1,1 ===============================
print("\n N-1 ")
def sorte_numbers(numbers:list):
    new_numbers = list(filter(lambda x: x % 2 == 0, numbers))
    return new_numbers

numbers = [1,2,3,4,5,6,8,22,55]
res1 = sorte_numbers(numbers)
print(res1)


# ============================== 2 ===============================
print("\n N-2 ")



def get_new_list(liste_of_persons:list):
   new_list = list(sorted(liste_of_persons, key=lambda x: x[1]))
   return new_list

persons = [("Dmitry",26), ("Oleg",30), ("Sergey", 18), ("Mariya", 15)]
res2 = get_new_list(persons)
print(res2)


# ============================== 3 ===============================
print("\n N-3 ")


def get_new_string(lists_of_string: list):
   vowels = ("аеиоуыэюя")
   new_string = list(filter(lambda x: x[0] in vowels, lists_of_string))
   return new_string,



list_of_string = ["напишите код, который принимает","используйте функцию filter и множество",
                  "возвращает новый список", "отсортированный по убыванию длины слов"]
res3 = get_new_string(list_of_string)
print(res3)

# ============================== 4 ===============================
print("\n N-5 ")


def get_new_list(numbs:list):
    new_list_of_numbs = list(map(lambda x:x**2,numbs))
    return new_list_of_numbs


numbs = [2,5,6,12,20,7,8]
res4 = get_new_list(numbs)
print(res4)


# ============================== 5 ===============================
print("\n N-5 ")


def get_new_words(words:list):
    new_list_len_words = list(sorted(words, key=lambda x: len(x), reverse=True))
    return new_list_len_words


l_words = ["Напишите","код", "который", "принимает", "список", "чисел", "и", "возвращает", "новый", "список",
"содержащий", "эти", "же", "числа"]
res5 = get_new_words(l_words)
print(res5)


# ============================== 6 ===============================
def get_words_in_python(text_of_python: str):

    word_py = set("python")
    coincidences_letters = list(filter(lambda i: i in word_py, text_of_python))

    return coincidences_letters


text = (" My family is a rather small one, with only three people,"
        " my father, my mother and me. My father is a doctor."
        " My mother is a middle-school teacher")
res6 = get_words_in_python(text)
print(res6)


# ============================== 7 ===============================
print("\n N-7 ")


def get_new_list(numbs:list):
    new_list_of_numbs = list(map(lambda x:x*10,numbs))
    return new_list_of_numbs


numbs = [2,5,6,12,20,7,8]
res7 = get_new_list(numbs)
print(res7)


# ============================== 8 ===============================
print("\n N-8 ")


def get_new_words(words:list):
    new_list_len_words = list(sorted(words))
    return new_list_len_words


l_words = ["Напишите","код", "который", "принимает", "список", "чисел", "и", "возвращает", "новый", "список",
"содержащий", "эти", "же", "числа"]
res5 = get_new_words(l_words)
print(res5)

# ============================== 9 ===============================
print("\n N-9")


def get_polindrom(list_with_texts:list):
    polindrom_list = list(filter(lambda i: i == i[::-1], list_with_texts))
    return polindrom_list



list_with_texts = ["Напишите код, который принимает список ", "которое читается одинаково слева направо",
                   "а роза упал а н а лапу азор а", "содержащий квадраты этих чисел"]
res9 = get_polindrom(list_with_texts)
print(res9)


# ============================== 10 ===============================
print("\n N-10")


def get_list_vowels(list_with_words:list):
    vowels = set("аеиоуыэюя")
    new_list = sorted(list_with_words, key=lambda x: sum(c in vowels for c in x))
    return new_list


random_words = ["Напишите","код", "который", "принимает", "список", "чисел", "и", "возвращает", "новый", "список",
"содержащий", "эти", "же", "числа", "да", "а"]
res10 = get_list_vowels(random_words)
print(res10)


# ============================== 11 ===============================
print("\n N-11")


def get_upper_list(list_of_text: list):
    upper_list = list(map(str.upper, list_of_text))
    return upper_list


list_of_texts = ["Напишите код, который принимает список ", "которое читается одинаково слева направо",
                       "а роза упал а н а лапу азор а", "содержащий квадраты этих чисел"]
res11= get_upper_list(list_of_texts)
print(res11)

# ============================== 12 ===============================
print("\n N-12")


def get_hello_list(list_of_text: list):
    hello = " Hello "
    hello_list = list(map(lambda i: str(hello) + str(i), list_of_text))


    return hello_list


list_of_texts = ["Напишите код, который принимает список ", "которое читается одинаково слева направо",
                       "а роза упал а н а лапу азор а", "содержащий квадраты этих чисел"]
res11= get_hello_list(list_of_texts)
print(res11)

# ============================== 13 ===============================
print("\n N-13")

def get_list_a(list_with_words:list):
    a = "а"
    new_list_a = sorted(list_with_words, key=lambda x:sum(c in a for c in x),reverse=True)
    return new_list_a


random_words = ["Напишите","код", "который", "принимает", "список", "чисел", "и", "возвращает", "новый", "список",
"содержащий", "эти", "же", "числа", "да", "а"]
res13 = get_list_a(random_words)
print(res13)

# ============================== 14 ===============================
print("\n N-14")

def get_list_unique(list_with_words:list):
    unique_letters = "йьъё"
    new_list_a = sorted(random_words, key=lambda x: len(set(x)),reverse=True)
    #new_list_a = sorted(set(random_words), key=lambda x: sum(c in unique_letters for c in set(x)),reverse=True)

    return new_list_a


random_words = ["Напишите","код", "котойрйый", "принимает", "список", "чисел", "и", "возвращаетьъъ", "новый", "список",
"содержащий", "эти", "же", "числа", "да", "а"]
res14 = get_list_unique(random_words)
print(res14)



# ============================== 15 ===============================
print("\n N-15")


def decorator(func):
    def wrapper(*args, **kwargs):
        print("функция до враппера ", args,  kwargs)
        for x in range(1,6):
            func(text)
        res = func(*args, **kwargs)
        print(f" {res} \n  результат функции(после враппера) ")
        return res

    return wrapper



@ decorator
def get_words_in_python(text_of_python: str):
    word_py = set("python")
    coincidences_letters = list(filter(lambda i: i in word_py, text_of_python))
    return coincidences_letters



text = (" My family is a rather small one")
get_words_in_python(text)
hello




