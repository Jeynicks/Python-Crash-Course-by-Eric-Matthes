"""9-2. Three Restaurants: Start with your class from Exercise 9-1. Create three
different instances from the class, and call describe_restaurant() for each
instance."""

class Restaurant():
    
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    
    def describe_restaurant(self):
        print(f"Restaurant Name: {self.restaurant_name}\n"+
              f"Cuisine Type: {self.cuisine_type}")
    
    def open_restaurant(self):
        print("Restaurant is Open!")

Jollibee = Restaurant('Jollibee', 'Filipino Cuisine')
Mcdonalds = Restaurant('Mcdonalds', 'American Cuisine')
Kentucky_Fried_Chicken = Restaurant('KFC', 'American Cuisine')

Jollibee.describe_restaurant()
Mcdonalds.describe_restaurant()
Kentucky_Fried_Chicken.describe_restaurant()

        