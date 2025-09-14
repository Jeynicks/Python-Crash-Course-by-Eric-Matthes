"""10-3. Guest: Write a program that prompts the user for their name. When they
respond, write their name to a file called guest.txt"""

file_path = 'Chapter 10 - Files and Exceptions\\Exercise 10-3\\guest.txt'

with open(file_path, 'w') as guest_file:
    name = input('Enter Username: ')
    guest_file.write(name)