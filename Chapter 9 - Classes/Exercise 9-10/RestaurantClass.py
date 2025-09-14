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