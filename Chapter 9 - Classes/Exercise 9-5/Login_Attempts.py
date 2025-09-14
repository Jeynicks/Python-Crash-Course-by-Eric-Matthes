"""9-5. Login Attempts: Add an attribute called login_attempts to your User
class from Exercise 9-3 (page 166). Write a method called increment_
login_attempts() that increments the value of login_attempts by 1. Write
another method called reset_login_attempts() that resets the value of login_
attempts to 0.
Make an instance of the User class and call increment_login_attempts()
several times. Print the value of login_attempts to make sure it was incremented
properly, and then call reset_login_attempts(). Print login_attempts again to
make sure it was reset to 0"""

class User():
    
    def __init__(self, first_name, last_name, age, gender):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender
        self.login_attempts = 0
        
    def describe_user(self):
        full_name = self.first_name + ' ' + self.last_name
        print(f"Full Name: {full_name}\n"+
              f"Age: {self.age}\n"+
              f"Gender: {self.gender}")
        
    def greet_user(self):
        full_name = self.first_name + ' ' + self.last_name
        print(f"Hello {full_name}, nice to meet you!") 
    
    def increment_login_attempts(self):
        self.login_attempts += 1
        
    def reset_login_attempts(self):
        self.login_attempts = 0
        
user1 = User('Python', 'Jeynicks', 20, 'Male')
print(f"Login Attempts: {user1.login_attempts}")
user1.increment_login_attempts()   
user1.increment_login_attempts()   
user1.increment_login_attempts()   
user1.increment_login_attempts()   
user1.increment_login_attempts()   
print(f"Login Attempts: {user1.login_attempts}")
user1.reset_login_attempts()
print(f"Login Attempts: {user1.login_attempts}")         
            