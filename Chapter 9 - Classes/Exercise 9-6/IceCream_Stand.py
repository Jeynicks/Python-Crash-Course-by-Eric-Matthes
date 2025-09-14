"""9-6. Ice Cream Stand: An ice cream stand is a specific kind of restaurant. Write
a class called IceCreamStand that inherits from the Restaurant class you wrote
in Exercise 9-1 (page 166) or Exercise 9-4 (page 171). Either version of
the class will work; just pick the one you like better. Add an attribute called
flavors that stores a list of ice cream flavors. Write a method that displays
these flavors. Create an instance of IceCreamStand, and call this method"""

class Restaurant():
    
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    
    def describe_restaurant(self):
        print(f"Restaurant Name: {self.restaurant_name}\n"+
              f"Cuisine Type: {self.cuisine_type}")
    
    def open_restaurant(self):
        print("Restaurant is Open!")
    
    def set_number_served(self, customer_served):
        self.number_served = customer_served
    
    def increment_number_served(self, add_customer):
        self.number_served += add_customer    
        
class IceCreamStand(Restaurant):
    
    def __init__(self, restaurant_name, cuisine_type, flavors: list):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors
    
    def display_flavors(self):
        print(f"{self.restaurant_name}'s Ice Cream Flavors: ")
        for flavor in self.flavors:
            print("- " + flavor)                
        
selecta = IceCreamStand('Selecta', 'IceCream', ['Chocolate', 'Vanilla', 'Strawberry'])
selecta.display_flavors() 
 
        
