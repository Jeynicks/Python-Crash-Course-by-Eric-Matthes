"""9-8. Privileges: Write a separate Privileges class. The class should have one
attribute, privileges, that stores a list of strings as described in Exercise 9-7.
Move the show_privileges() method to this class. Make a Privileges instance
as an attribute in the Admin class. Create a new instance of Admin and use your
method to show its privileges"""

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
        
class Admin(User):
    def __init__(self, first_name, last_name, age, gender, ):
        super().__init__(first_name, last_name, age, gender)
        self.priviliges = Privilige()

class Privilige():
    def __init__(self, priviliges= ["can add post", "can delete post", "can ban user"]):
        self.priviliges = priviliges
    
    def show_priviliges(self):
        print("Admin Priviliges: ")
        for privilige in self.priviliges:
            print("- " + privilige) 
            
admin = Admin('Jeynicks', 'Python', 20, 'Male')
admin.priviliges.show_priviliges()               
               