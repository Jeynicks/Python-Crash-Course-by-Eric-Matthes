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