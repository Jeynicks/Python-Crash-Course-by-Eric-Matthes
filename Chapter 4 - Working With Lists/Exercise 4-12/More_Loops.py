"""4-12. More Loops: All versions of foods.py in this section have avoided using
for loops when printing to save space. Choose a version of foods.py, and
write two for loops to print each list of foods."""

pizzas = ['Pepperoni Pizza', 'BBQ Chicken Pizza', 'Bacon Pizza']
friend_pizzas = pizzas[:]

pizzas.append('Cheesy Pizza')
friend_pizzas.append('Pineapple Pizza')

print("My Favorite Pizzas are:")
for pizza in pizzas:
    print(pizza)
print()
    
print("My Friends Favorite Pizzas are: ")
for pizza in friend_pizzas:
    print(pizza)    