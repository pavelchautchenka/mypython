# ============================== 1 ===============================
print("\n N-1 ")


def root(x):
    return x**2


res1 = root(2)
print(res1)

# ============================== 2 ===============================
print("\n N-2 ")


def is_even(n):
    return n % 2 == 0


res2 = is_even(6)
print(res2)
# ============================== 3 ===============================
print("\n N-3 ")


def factorial(a):
    fac = 1
    if a > 0:
        for i in range(2, a + 1):
            fac *= i
        return fac
    elif a ==0:
        return 0
    else:
        return -1


res3 = factorial(3)
print(res3)
# ============================== 4 ===============================
print("\n N-4 ")

def reverse(s):
    reversed = s[::-1]
    return reversed


res4 = reverse("hello")
print(res4)
# ============================== 5 ===============================
print("\n N-5 ")


def fibonacci(e):
    a = 0
    b = 1
    for i in range(e):
        a,b = b,a+b
    return a

res5 = fibonacci(6)
print(res5)
# ============================== 6 ===============================
print("\n N-6 ")


def count_vowels(r):

    vowels = set("аеёиоуыэюя")
    count = 0

    for i in r:
        if i in vowels:
            count += 1
    return count


res6 = count_vowels("приветули")
print(res6)
# ============================== 7 ===============================
print("\n N-7 ")

def is_palindrome(t):
    t_renverse = t[::-1]
    if t == t_renverse:
        return True
    else:
        return False

res7 = is_palindrome("топот")
print(res7)
# ============================== 8 ===============================
print("\n N-8 ")


def power(y,u):
    return y**u


res8 = power(5,2)
print(res8)
# ============================== 9 ===============================
print("\n N-9 ")
def is_anagram(s1,s2):
    if len(s1) == len(s2):
        return set(s1.lower()) == set(s2.lower())
    else:
        return False


res10 = is_anagram("кот", "ток")
print(res10)
# ============================== 10 ===============================
print("\n N-10 ")
def is_pangram (s):
    alphabet = ('абвгдеёжзийклмнопрстуфхцчшщъыьэюя')
    symbols_to_remove = ",!?. "
    for symbol in symbols_to_remove:
        s = s.replace(symbol, "")
    return set(alphabet.lower()) == set(s.lower())


res10 = is_pangram("аэрофотосъёмка ландшатфа уже выявила земли богачей и процветающих крестьян.")
print(res10)

# ============================== 10.2 способ =====================
def is_pangram (s):
    alphabet = set('абвгдеёжзийклмнопрстуфхцчшщъыьэюя')

    for symbol in alphabet:
        if symbol not in s.lower():
            return False
    else:
        return True

res10 = is_pangram("аэрофотосъёмка ландшатфа уже выявила земли богачей и процветающих крестьян")
print(res10)