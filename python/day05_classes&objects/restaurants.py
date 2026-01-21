class restaurant:
    pass
bobs_burger=restaurant()
bobs_burger.name='Bob\'s Burgers'
bobs_burger.cuisine='American Diner'
bobs_burger.rating=4.7
bobs_burger.parcel=False
italian_pizza=restaurant()
italian_pizza.name='Italian Pizza'
italian_pizza.cuisine='Italian'
italian_pizza.rating=4.8
italian_pizza.parcel=True
print(vars(bobs_burger))
print(vars(italian_pizza))
