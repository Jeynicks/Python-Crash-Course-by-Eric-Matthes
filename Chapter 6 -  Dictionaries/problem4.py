"""6-4. Glossary 2: Now that you know how to loop through a dictionary, clean
up the code from Exercise 6-3 (page 102) by replacing your series of print
statements with a loop that runs through the dictionary’s keys and values.
When you’re sure that your loop works, add five more Python terms to your
glossary. When you run your program again, these new words and meanings
should automatically be included in the output"""

glossary = {
    'Variables': 'Is something that stores data',
    'Lists': 'Is a datatype where we can store more values',
    'If Statements': 'Is used to determine if a condition is True',
    'Dictionaries': "It's like a list but has keys and value" 
}

for word, meaning in glossary.items():
    print(f"{word} - \n\t{meaning}")