import package


coffee1 = package.Coffee(1225, "cappuccino", 12, 'M')

coffee2 = package.Coffee(1114, "espresso", 7, "S")
pizza1 = package.Pizza(122, "margarita", 20, 35, 'with filling')
my_shop = package.RealShop()
my_shop.add_product(coffee2)
my_shop.add_product(coffee1)
my_shop.add_product(pizza1)
my_shop.sell_product(coffee2)

print(my_shop.all_products())


fur_shop = package.FurnitureShop()
table1 = package.Table(12, "azea", 520, 'big table', 'round')
chair1 = package.Chair(13, 'sdqdq', 640, 'venge', 'wood')
locker1 = package.Locker(14, "dqsqd", 760, "steel", 'small')
fur_shop.add_product(table1)
fur_shop.add_product(chair1)
fur_shop.add_product(locker1)
fur_shop.sell_product(locker1)


print(fur_shop.all_products())


comp_shop = package.ComputerShop()
comp1 = package.Mothercard(12, 'sqd', 125, 128, 'mem')
comp2 = package.Mothercard(12, 'sqd', 125, 128, 'mem')
comp_shop.add_product(comp1)
comp_shop.add_product(comp2)
print(comp_shop.all_products())