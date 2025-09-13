"""6-10. Favorite Numbers: Modify your program from Exercise 6-2 (page 102) so
each person can have more than one favorite number.Then print each person’s
name along with their favorite numbers."""

favorite_num = {
    'Jeynicks': [36, 5, 19],
    'Nikaniks': [24, 8, 6],
    'Stephen Curry': [30, 4, 31],
    'Lebron James': [23, 6, 9],
    'Derrick Rose': [1, 0, 2]
}

for names, num in favorite_num.items():
    print(f"{names}'s favorite number is {num}")