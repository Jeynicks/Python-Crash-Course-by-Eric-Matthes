"""10-6. Addition: One common problem when prompting for numerical input
occurs when people provide text instead of numbers. When you try to convert
the input to an int, you’ll get a TypeError. Write a program that prompts for
two numbers. Add them together and print the result. Catch the TypeError if
either input value is not a number, and print a friendly error message. Test your
program by entering two numbers and then by entering some text instead of a
number."""

try:
    num1 = input('Enter 1st num: ')
    num2 = input('Enter 2nd num: ')
    sum = int(num1) + int(num2)

    
except ValueError: # Am I trippin or this should be ValueError
    print('Must Enter an Integer')
    
else:
    print("The sum of 2 numbers: " + str(sum))    