"""7-4. Pizza Toppings: Write a loop that prompts the user to enter a series of
pizza toppings until they enter a 'quit' value. As they enter each topping,
print a message saying you’ll add that topping to their pizza."""


message = "Enter Toppings\nEnter 'quit' if you want to exit: "
response = ''

while response != 'quit':   
    response = input(message)
        
    if response != 'quit':
        print(f"We'll add {response} topping to your pizza\n")    
    