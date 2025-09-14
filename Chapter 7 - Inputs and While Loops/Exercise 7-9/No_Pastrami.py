"""7-9. No Pastrami: Using the list sandwich_orders from Exercise 7-8, make sure
the sandwich 'pastrami' appears in the list at least three times. Add code
near the beginning of your program to print a message saying the deli has
run out of pastrami, and then use a while loop to remove all occurrences of
'pastrami' from sandwich_orders. Make sure no pastrami sandwiches end up
in finished_sandwiches."""

sandwich_orders = ['Tuna', 'Pastrami', 'Peanut Butter and Jam', 'Pastrami', 'Choco', 'Cheese', 'Ham', 'Bacon', 'Pastrami']
finished_sandwiches = []

print("Deli has ran out of pastrami")

while sandwich_orders:   
    
    if 'Pastrami' in sandwich_orders:
        sandwich_orders.remove('Pastrami')
    
    print(f"I made your {sandwich_orders[0]} Sandwich")
    current_sandwich = sandwich_orders.pop(0)
    finished_sandwiches.append(current_sandwich)
    
print(f"Finished sandwiches: {finished_sandwiches}")  