"""9-7. Admin: An administrator is a special kind of user. Write a class called
Admin that inherits from the User class you wrote in Exercise 9-3 (page 166)
or Exercise 9-5 (page 171). Add an attribute, privileges, that stores a list
of strings like "can add post", "can delete post", "can ban user", and so on.
Write a method called show_privileges() that lists the administrator’s set of
privileges. Create an instance of Admin, and call your method."""

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
    def __init__(self, first_name, last_name, age, gender, priviliges= ["can add post", "can delete post", "can ban user"]):
        super().__init__(first_name, last_name, age, gender)
        self.priviliges = priviliges
        
    def show_priviliges(self):
          print(f"{self.first_name}'s Admin Priviliges:")
          for privilige in self.priviliges:
              print("- " + privilige)
            
                
admin = Admin('Jeynicks', 'Python', 20, 'Male')
admin.show_priviliges()