"""10-2. Learning C: You can use the replace() method to replace any word in a
string with a different word. Here’s a quick example showing how to replace
'dog' with 'cat' in a sentence:
>>> message = "I really like dogs."
>>> message.replace('dog', 'cat')
'I really like cats.'
Read in each line from the file you just created, learning_python.txt, and
replace the word Python with the name of another language, such as C. Print
each modified line to the screen."""

file_name = 'C:\\Users\\63935\Desktop\\Python Crash Course by Eric Matthes\\Chapter 10 - Files and Exceptions\\learning_python.txt'

with open(file_name) as file_object:
    contents = file_object.read()
    contents = contents.replace('Python', 'LUA') 
    
    print(contents) 
