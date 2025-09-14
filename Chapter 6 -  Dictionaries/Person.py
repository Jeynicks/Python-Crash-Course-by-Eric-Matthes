"""6-1. Person: Use a dictionary to store information about a person you know.
Store their first name, last name, age, and the city in which they live. You
should have keys such as first_name, last_name, age, and city. Print each
piece of information stored in your dictionary."""

personal_info = {
    "first_name": "John",
    "last_name": "Doe",
    "age": 36,
    "city": "Daytona"    
}

for key, value in personal_info.items():
    print(key, value)
