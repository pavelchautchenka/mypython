import shops


coffee1 = shops.typess.Coffee(1225, "cappuccino", 12, 'M')
coffee2 = shops.typess.Coffee(1114, "espresso", 7, "S")
pizza1 = shops.typess.Pizza(122, "margarita", 20, 35, 'with filling')
my_shop = shops.RealShop()
my_shop.add_product(coffee2)
my_shop.add_product(coffee1)
my_shop.add_product(pizza1)
my_shop.sell_product(coffee2)
print(my_shop.all_products())


fur_shop = shops.FurnitureShop()
table1 = shops.typess.Table(12, "azea", 520, 'big table', 'round')
chair1 = shops.typess.Chair(13, 'sdqdq', 640, 'venge', 'wood')
locker1 = shops.typess.Locker(14, "dqsqd", 760, "steel", 'small')
fur_shop.add_product(table1)
fur_shop.add_product(chair1)
fur_shop.add_product(locker1)
fur_shop.sell_product(locker1)


print(fur_shop.all_products())


comp_shop = shops.ComputerShop()
comp1 = shops.typess.Mothercard(12, 'sqd', 125, 128, 'mem')
comp2 = shops.typess.Mothercard(12, 'sqd', 125, 128, 'mem')
comp_shop.add_product(comp1)
comp_shop.add_product(comp2)
print(comp_shop.all_products())
