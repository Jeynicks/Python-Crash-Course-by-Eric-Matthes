"""10-7. Addition Calculator: Wrap your code from Exercise 10-6 in a while loop
so the user can continue entering numbers even if they make a mistake and
enter text instead of a number."""

active = True
while active:    
    try:
        num1 = input('Enter 1st num: ')
        num2 = input('Enter 2nd num: ')
        sum = int(num1) + int(num2)
        
    except ValueError: # Am I trippin or this should be ValueError
        print('Must Enter an Integer')
    
    else:    
        print("The sum of 2 numbers: " + str(sum))  
        active = False   

