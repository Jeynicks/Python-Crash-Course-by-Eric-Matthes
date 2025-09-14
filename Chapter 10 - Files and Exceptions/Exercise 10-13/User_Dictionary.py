"""10-13. User Dictionary: The remember_me.py example only stores one piece of
information, the username. Expand this example by asking for two more pieces
of information about the user, then store all the information you collect in a
dictionary. Write this dictionary to a file using json.dumps(), and read it back
in using json.loads(). Print a summary showing exactly what your program
remembers about the user"""

from pathlib import Path
import json

user_path = Path('user.json')
user_info = {}

if user_path.exists():
    contents = user_path.read_text()
    user_info = json.loads(contents)
    
    for key, value in user_info.items():
        print(f"{key}: {value}")
        
         
    
else:
    username = input('Enter username: ')
    age = input('Enter age: ')
    gender = input('Enter gender: ')
    

    user_info['username'] = username
    user_info['age'] = age
    user_info['gender'] = gender
    
    contents = json.dumps(user_info)
    
    user_path.write_text(contents)

