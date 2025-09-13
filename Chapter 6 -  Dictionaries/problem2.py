"""6-2. Favorite Numbers: Use a dictionary to store people’s favorite numbers.
Think of five names, and use them as keys in your dictionary. Think of a favorite
number for each person, and store each as a value in your dictionary. Print
each person’s name and their favorite number. For even more fun, poll a few
friends and get some actual data for your program."""

favorite_num = {
    'Jeynicks': 36,
    'Nikaniks': 24,
    'Stephen Curry': 30,
    'Lebron James': 23,
    'Derrick Rose': 1
}

for names, num in favorite_num.items():
    print(f"{names}'s favorite number is {num}")

