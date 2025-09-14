"""9-4. Number Served: Start with your program from Exercise 9-1 (page 166).
Add an attribute called number_served with a default value of 0. Create an
instance called restaurant from this class. Print the number of customers the
restaurant has served, and then change this value and print it again.
Add a method called set_number_served() that lets you set the number
of customers that have been served. Call this method with a new number and
print the value again.
Add a method called increment_number_served() that lets you increment
the number of customers who’ve been served.
Call this method with any number you like that could represent how many customers were served in, say, a
day of business"""

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
        
restaurant = Restaurant('Jollibee', 'Filipino Cuisine')   
     
print(f"Customer Served: {restaurant.number_served}") 

restaurant.set_number_served(100)
print(f"Customer Served: {restaurant.number_served}")        
        
restaurant.increment_number_served(10)
print(f"Customer Served: {restaurant.number_served}")        
