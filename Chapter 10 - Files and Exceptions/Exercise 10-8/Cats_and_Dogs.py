"""10-8. Cats and Dogs: Make two files, cats.txt and dogs.txt. Store at least three
names of cats in the first file and three names of dogs in the second file. Write
a program that tries to read these files and print the contents of the file to the
screen. Wrap your code in a try-except block to catch the FileNotFound error,
and print a friendly message if a file is missing. 
Move one of the files to a different location on your system, and make sure the code in the except block
executes properly."""

def read_file(file_path):
    try:
        with open(file_path) as file:
            contents = file.read()
            
    except FileNotFoundError:
        print(f"{file_path} not Found!")
        
    else:
        print(contents)    
                


file_path_list = [
    'Chapter 10 - Files and Exceptions\\Exercise 10-8\\cats.txt',
    'Chapter 10 - Files and Exceptions\\Exercise 10-8\\dogs.txt'
]

for file in file_path_list:
    read_file(file)
                

