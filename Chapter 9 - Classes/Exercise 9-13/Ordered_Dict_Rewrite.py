"""9-13. OrderedDict Rewrite: Start with Exercise 6-4 (page 108), where you
used a standard dictionary to represent a glossary. Rewrite the program using
the OrderedDict class and make sure the order of the output matches the order
in which key-value pairs were added to the dictionary"""

from collections import OrderedDict

glossary = OrderedDict()

glossary['Variables'] = 'Is something that stores data'
glossary['Lists'] = 'Is a datatype where we can store more values'
glossary['If Statement'] = 'Is used to determine if a condition is True'
glossary['Dictionaries'] = "It's like a list but has keys and value" 

for word, description in glossary.items():
    print(f"{word}\n- {description}")
