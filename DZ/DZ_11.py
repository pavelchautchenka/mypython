# ============================== 1 ===============================
print("\n N-1 ")


class Soda:

    def __init__(self, name_of_addition: str = None):
        self.name_of_addition = name_of_addition

    def show_me_drink(self):
        if self.name_of_addition is None:
            print("simple Soda")
        else:
            print(f"soda with {self.name_of_addition.upper()}")


s1 = Soda()
s1.show_me_drink()

# ============================== 2 ===============================
print("\n N-2 ")


class TriangleChecker:
    def __init__(self, a: int | float, b: int | float, c: int | float):
        self.a = a
        self.b = b
        self.c = c

    @staticmethod
    def is_triangle(a, b, c):
        if type(a) not in (int, float) or type(b) not in (int,float) or type(c) not in (int, float):
        #if type (a or b or c) not in (int,float):--------------  >
        #if isinstance(a and b and c, (int, float)) is False: --  >   Почему так не работает ?
        # if isinstance((a,b,c), (int, float)) is False:--------  >
            return "Only need to enter numbers"
        elif a <= 0 or b <= 0 or c <= 0:
            return "Nothing will work with negative numbers!"
        elif a + b < c or a + c < b or b + c < a:
            return "It's a pity, but you can't make a triangle out of this"
        else:
            return "Hurray, you can build a triangle!"


tr1 = TriangleChecker.is_triangle(1, 2, 3)
print(tr1)



# ============================== 3/1 ===============================
print("\n N-3 ")



class KgToPounds:
    def __init__(self, kg: int | float):
        self.__kg = kg

    def to_pound(self):
        return self.__kg * 2.2

    def set_kg(self, new_kg: int | float):
        if type(new_kg) in (int, float):
            self.__kg = new_kg

    def get_kg(self):
        return self.__kg

# ============================== 3/2 ===============================


class KgToPounds:
    def __init__(self, kg: int | float):
        self.__kg = kg

    def to_pound(self):
        return self.__kg * 2.2

    @property
    def get_kg(self):
        return self.__kg

    @get_kg.setter
    def get_kg(self, new_kg: int | float):
        if type(new_kg) in (int, float):
            self.__kg = new_kg



# ============================== 4 ===============================
class RealSting:
    def __init__(self, strings: str = " "):
        self.strings = strings

    def __lt__(self, other):
        return len(self.strings) < len(other.strings)

    def __le__(self, other):
        return len(self.strings) <= len(other.strings)

    def __eq__(self, other):
        return len(self.strings) == len(other.strings)

    def __ne__(self, other):
        return len(self.strings) != len(other.strings)

    def __gt__(self, other):
        return len(self.strings) > len(other.strings)

    def __ge__(self, other):
        return len(self.strings) >= len(other.strings)


s1 = RealSting("1225")
s2 = RealSting('qsddqsdq')
print(s1 < s2)

print(RealSting('hi') == RealSting('hello'))


# ============================== 5 ===============================
print("\n N-5 ")

class Rectangle:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height


    def str(self):
        return f"ractangle with {self.width} \n " \
               f"and height {self.width}"

    def get_area(self):
        return self.width * self.height
    @staticmethod
    def perimetr(width,height):
        return width*2 + height*2

    @property
    def is_square(self):
        if self.height == self.width:
            return False
        else:
            return True

rec1 = Rectangle(5,6)
print(rec1.get_area())

rec2 = Rectangle(10,7)
print(rec2.get_area())

print(rec2.perimetr(5,9))

print(rec2.is_square)

# ============================== 6 ===============================
print("\n N-6 ")


class Person:
    def __init__(self, name: str, age: int, gender: str):
        self.name = name
        self.age = age
        self.gender = gender

    def str(self):
        return f"Имя:{self.name} Возраст:{self.age} Пол:{self.gender}"

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name: str):
        self.__name = new_name

    #@property
    #def set_name(self, new_name):             ====> или так лучше записать ?
        #self.__name = new_name

    @staticmethod
    def is_adulte(age):
        if age >= 18:
            return True
        else:
            return False

    @classmethod
    def crate_from_string(cls, s: str):
        name, age, gender = s.split("-")
        my_date = cls(name, age, gender)
        return my_date


p1 = Person("pashka",20,"M")
p1.name = "oleg"
print(p1.age)
print(p1.is_adulte(17))

p3 = Person.crate_from_string("Dima-25-M")

print(type(p3))
print(p3.str())
