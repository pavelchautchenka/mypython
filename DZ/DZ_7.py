
# ============================== 1 ===============================
print("\n N-1 ")


def make_sentence(words: list = None):
    if words is None:
        words = ["This", "is", "a", "sentence"]
    print(' '.join(words) + ".")


make_sentence(words=["Python", "is", "fun"])
make_sentence()

# ============================== 2 ===============================
print("\n N-2 ")


def sum_of_squares(*numbers: int):
    sum = 0
    for number in numbers:
        sum += number ** 2
    return sum


res2 = sum_of_squares(1, 2, 3, 5, 6)
print(res2)
# ============================== 3 ===============================
print("\n N-3 ")


def greet(name:str = None, language:str = 'en'):
    languages = {'en': 'hello',
                 'fr': 'Bonjour',
                 'ru': 'Privet'}
    print(languages[language], ",", name, "!")


greet(name='Anna',language='fr')


# ============================== 4 ===============================
print("\n N-4 ")


def print_info(**kwargs):
    if not kwargs:
        print("No info given")
        return

    for key, value in kwargs.items():
        print("{} : {}".format(key, value))


print_info(name="Alex", age=25, city="Amsterdam")
print_info()


# ============================== 5 ===============================
print("\n N-5 ")


def print_info(**kwargs):
    if not kwargs:
        print("No info given")
        return

    print(f"""
|   key   |   value   |
|---------|-----------|  """)
    for key, value in kwargs.items():
        print(f"|  {key:<7}| {value:<10}|")


print_info(name="Alex", age=25, city="Amsterdam")
print_info()

# ============================== 6 ===============================
print("\n N-6 ")

def calculate(*args, operation="+"):
    if operation == "+":
        count= 0
        for i in args:
            count += i
        print(count)
    elif operation == "-":
        count = 0
        for i in args:
            count -= i
        print(count)
    elif operation == "*":
        count = 1
        for i in args:
            count *= i
        print(count)
    elif operation == '/':
        count = args[0]
        for i in args[1:]:
            count = count / i
        print(count)
    else:
        print('неизвестный знак')

calculate(1,2,3,4,operation="+")

# ============================== 7 ===============================
print("\n N-7 ")


def print_triangl(height:int = 5):
    i = 1
    height = height + height-1

    while i <= height:
        print((i*"*").center(50))
        i+=2

print_triangl(10)


# ============================== 7/2 ===============================
print("\n N-7/2 ")


def print_triangl(height:int = 5):
    i = 1
    while i <= height + height-1:
        print(f"{i *'*':^50}")
        i+=2

print_triangl(10)

# ============================== 8 ===============================
print("\n N-8 ")

def create_post(title:str,content:str,author:str,category:str = "general"):
    post = {"title": title,
            "content": content,
            "author": author,
            "category": category}
    print(post)
create_post(title='new_chapter',content='Comedy',author='Oleg',category='live')

# ============================== 9 ===============================
print("\n N-9 ")
def create_product(name:str,price:float,category:str,rating:float=0):
    article ={"name": name,
              "price": price,
              "category": category,
              "rating":rating}
    print(article)

create_product(name="stylo", price=22.5, category="buro",rating= 4.1)

# ============================== 10 ===============================
print("\n N-10 ")
def create_student(name:str, last_name:str, surname:str,group: int, date_of_entrance:str = "19.10.2023",
                    gpa:float=None,semester:int = None, telephone:int= None, address:str = None):
    student = {'name':name,
               'laste_name':last_name,
               'surname':surname,
               'group':group,
               'date_of_entrence':date_of_entrance,
               'gpa': gpa,
               'semester': semester,
               'telephone':telephone,
               'address': address}

    if student.get('gpa')  == None:
        del student['gpa']
    if student.get('semester')  == None:
        del student['semester']
    if student.get('telephone')  == None:
        del student['telephone']
    if student.get('address')  == None:
        del student['address']
    print(student)


create_student(name="Oleg", last_name="Ivanov", surname="Ivanovich", group=5,date_of_entrance= "01.09.2020",gpa=2)

# ============================== 10/2 ===============================
print("\n N-10/2 ")


def create_student(name:str, last_name:str, surname:str,group: int, date_of_entrance: str = "19.10.2023", **kwargs):
    student = {'name':name,
               'laste_name':last_name,
               'surname':surname,
               'group':group,
               'date_of_entrence':date_of_entrance}

    #student.update(kwargs)

    for key, value in kwargs.items():
        student[key] = value



    print(student)


create_student("Oleg", "Ivanov", "Ivanovich", 5, "01.09.2020", gpa=2, semester = 4)