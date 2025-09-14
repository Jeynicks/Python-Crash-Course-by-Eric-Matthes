"""10-9. Silent Cats and Dogs: Modify your except block in Exercise 10-8 to fail
silently if either file is missing."""

def read_file(file_path):
    try:
        with open(file_path) as file:
            contents = file.read()
            
    except FileNotFoundError:
        pass
        
    else:
        print(contents)    
                


file_path_list = [
    'Chapter 10 - Files and Exceptions\\Exercise 10-8\\cats.txt',
    'Chapter 10 - Files and Exceptions\\Exercise 10-8\\dogs.txt'
]

for file in file_path_list:
    read_file(file)
                