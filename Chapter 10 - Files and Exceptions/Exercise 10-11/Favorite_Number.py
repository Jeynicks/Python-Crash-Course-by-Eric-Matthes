"""10-11. Favorite Number: Write a program that prompts for the user’s favorite
number. Use json.dumps() to store this number in a file. 
Write a separate program that reads in this value and prints the message “I know your favorite
number! It’s _____.”"""

from pathlib import Path
import json

num = input('Enter your favorite number: ')

favorite_num = Path('favorite_number.json')
content = json.dumps(num)

favorite_num.write_text(num)
