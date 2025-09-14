"""9-3. Users: Make a class called User. Create two attributes called first_name
and last_name, and then create several other attributes that are typically stored
in a user profile. Make a method called describe_user() that prints a summary
of the user’s information. Make another method called greet_user() that prints
a personalized greeting to the user.
Create several instances representing different users, and call both methods
for each user."""

class User():
    
    def __init__(self, first_name, last_name, age, gender):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender
        
    def describe_user(self):
        full_name = self.first_name + ' ' + self.last_name
        print(f"Full Name: {full_name}\n"+
              f"Age: {self.age}\n"+
              f"Gender: {self.gender}")
        
    def greet_user(self):
        full_name = self.first_name + ' ' + self.last_name
        print(f"Hello {full_name}, nice to meet you!")        

user1 = User('Python', 'Jeynicks', 20, 'Male')
user2 = User('Python', 'Nikaniks', 19, 'Female')

user1.describe_user()
user1.greet_user()
print()
user2.describe_user()
user2.greet_user()