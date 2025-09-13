"""4-13. Buffet: A buffet-style restaurant offers only five basic foods. Think of five
simple foods, and store them in a tuple.
•	 Use a for loop to print each food the restaurant offers.
•	 Try to modify one of the items, and make sure that Python rejects the
change.
•	 The restaurant changes its menu, replacing two of the items with different
foods. Add a block of code that rewrites the tuple, and then use a for
loop to print each of the items on the revised menu."""

foods = ('Cheese Burger', 'Ham Burger', 'Choco Porridge', 'Double Choco', 'Chocolate')
print("The Restaurant offers: ")
for food in foods:
    print(food)

#foods[1] = 'Donut'    
print()
foods = ('Melted Choco', 'Choco Sundae', 'Choco Porridge', 'Double Choco', 'Chocolate')
print("Modified Foods: ")
for food in foods:
    print(food)