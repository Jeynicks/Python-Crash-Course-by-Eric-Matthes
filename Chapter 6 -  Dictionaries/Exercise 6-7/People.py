"""6-7. People: Start with the program you wrote for Exercise 6-1 (page 102).
Make two new dictionaries representing different people, and store all three
dictionaries in a list called people. Loop through your list of people. As you
loop through the list, print everything you know about each person"""

john_doe = {
    "first_name": "John",
    "last_name": "Doe",
    "age": 36,
    "city": "Daytona"    
}

noob_master = {
    "first_name": "Noob",
    "last_name": "Master",
    "age": 69,
    "city": "Ohio"  
}

python_jeynicks = {
    "first_name": "Python",
    "last_name": "Jeynicks",
    "age": 20,
    "city": "Paris"
}

peoples = [john_doe, noob_master, python_jeynicks]

for people in peoples:
    print(f"First Name: {people['first_name']}\n"+
          f"Last Name: {people['last_name']}\n"+
          f"Age: {people['age']}\n"+
          f"City: {people['city']}\n")
