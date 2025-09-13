"""5-1. Conditional Tests: Write a series of conditional tests. Print a statement
describing each test and your prediction for the results of each test. Your code
should look something like this:
car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')
print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')
•	 Look closely at your results, and make sure you understand why each line
evaluates to True or False.
•	 Create at least 10 tests. Have at least 5 tests evaluate to True and another
5 tests evaluate to False."""

"""5-2. More Conditional Tests: You don’t have to limit the number of tests you
create to 10. If you want to try more comparisons, write more tests and add
them to conditional_tests.py. Have at least one True and one False result for
each of the following:
•	 Tests for equality and inequality with strings
•	 Tests using the lower() function
•	 Numerical tests involving equality and inequality, greater than and
less than, greater than or equal to, and less than or equal to
•	 Tests using the and keyword and the or keyword
•	 Test whether an item is in a list
•	 Test whether an item is not in a list"""

#Test 1 and 2
food = 'Chocolate'
print("Is food == 'Chocolate'. I predict True.")
print(food == 'Chocolate')

print("Is food == 'Burger'. I predict False.")
print(food == 'Burger')

#Test 3 and 4
number = 36
print("Is number == 36 . I predict True.")
print(number == 36)

print("Is number == 24. I predict False.")
print(number == 24)

#Test 5 and 6
digit = 3.14
print("Is digit == 3.14. I predict True.")
print(digit == 3.14)

print("Is digit == 2.0. I predict False")
print(digit == 2.0)

#Test 7 and 8
gen1_pokemon = ['Bulbasaur', 'Squirtle', 'Charmander']
print("Is 'Charmander' in gen1_pokemon. I predict True")
print('Charmander' in gen1_pokemon)

print("Is 'Bidoof' in gen1_pokemon. I predict False.")
print('Bidoof' in gen1_pokemon)

#Test 9 and 10
xy_final_evo = ['Chesnaught', 'Delphox', 'Greninja']
print("Is 'Charizard' not in xy_final_evo. I predict True.")
print('Charizard' not in xy_final_evo)

print("Is 'Greninja' not in xy_final_evo. I predict False")
print('Greninja' not in xy_final_evo)