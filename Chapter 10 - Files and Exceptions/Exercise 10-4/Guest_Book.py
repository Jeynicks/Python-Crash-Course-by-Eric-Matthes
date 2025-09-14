"""10-4. Guest Book: Write a while loop that prompts users for their name. When
they enter their name, print a greeting to the screen and add a line recording
their visit in a file called guest_book.txt. Make sure each entry appears on a
new line in the file."""

file_path = 'Chapter 10 - Files and Exceptions\\Exercise 10-4\\guest_book.txt'

with open(file_path, 'a') as guest_book:
    
    while True:
        name = input("Enter Username or press 'q' to quit: ")
        
        if name == 'q':
            break
        
        print(f"Welcome {name}, It's nice to meet you")
        guest_book.write(f"{name} visited\n")