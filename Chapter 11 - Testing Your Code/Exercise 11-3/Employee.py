class Employee():
    """Employee class with First name, Last name and Annual salary as attribute"""
    
    def __init__(self, first_name, last_name, annual_salary):
        self.first_name = first_name
        self.last_name = last_name
        self.annual_salary = annual_salary
        
    def give_raise(self, raise_salary = 5000):
        self.annual_salary += raise_salary   
        return self.annual_salary