"""6-8. Pets: Make several dictionaries, where the name of each dictionary is the
name of a pet. In each dictionary, include the kind of animal and the owner’s
name. Store these dictionaries in a list called pets. Next, loop through your list
and as you do print everything you know about each pet."""

johnson = {
    'name': 'johnson',
    'species': 'dog',
    'age': 1,
}

ribombee = {
    'name': 'ribombee',
    'species': 'cat',
    'age': 1,
}

chunseo = {
    'name': 'chunseo',
    'species': 'cat',
    'age': 6,
}

pets = [johnson, ribombee, chunseo]

for pet in pets:
    print(f"Name: {pet['name'].title()}\n"+
          f"Species: {pet['species'].title()}\n"+
          f"Age: {pet['age']}\n")