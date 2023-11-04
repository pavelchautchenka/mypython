import time
# ============================== 1-2 ===============================
print("\n N-1-2 ")

class Auto:
    def __init__(self, brand:str, age: int, mark: str, color: str = " ", weight: int = 0):
        self.brand = brand
        self.age = age
        self.color = color
        self.mark = mark
        self.weight = weight

    def move(self):
        print('Move')

    def birthday(self):
        return self.age + 1

    def stop(self):
        print('stop')


class Truck(Auto):

    def __init__ (self, brand:str, age: int, mark: str,max_load: int, color: str = " ", weight: int = 0):
        self.max_load = max_load
        self.brand = brand
        self.age = age
        self.color = color
        self.mark = mark
        self.weight = weight

    def set_max_load(self, max_load):
        self.max_load = max_load
        return max_load

    def move(self):
        print("Attention", end=' ')
        super().move()

    def load(self):
        time.sleep(1)
        print("load")
        time.sleep(1)


class Car(Auto):
    def __init__(self, brand: str, age: int, mark: str, max_speed: int, color: str = " ", weight: int = 0,*args,**kwargs):
        super().__init__(brand, age, mark, color, weight, *args, **kwargs)
        self.max_speed = max_speed

    def move(self):
        time.sleep(1)
        print(f"move \n max speed is: {self.max_speed} km/h")
        time.sleep(1)


car1 = Car("audi", 50, "A4", 90)
print(car1.age)

car2 = Car("bmw", 20, "E30", 35)
car2.move()

truck1 = Truck("saab", 20, "z++", 750)
truck1.move()

truck2 = Truck("nissan", 3000, "z--",750, "red")
print(truck2.color)


# ============================== 3 ===============================
print("\n N-3 ")

class Point:
    def __init__(self, x: int | float, y: int | float):
        self.x = x
        self.y = y
class Circle:
    PI = 3.14

    def __init__(self,rad_one: int | float, rad_two: int | float):
        self.rad_one = rad_one
        self.rad_two = rad_two

    def calculation(self):
        res = abs(self.rad_one - self.rad_two)
        return res if res > 0 else Point(0, 0)


calcul1 = Circle(15, 10)
calcul1.calculation()