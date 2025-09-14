"""8-12. Sandwiches: Write a function that accepts a list of items a person wants
on a sandwich. The function should have one parameter that collects as many
items as the function call provides, and it should print a summary of the sandwich that is being ordered. 
Call the function three times, using a different number of arguments each time"""

def sandwich_maker(*fillings):
    print('Making sandwich with these fillings:')
    for filling in fillings:
        print('- '+str(filling))
        
sandwich_maker('Peanut Butter', 'Jam')
sandwich_maker('Bacon', 'Ham')
sandwich_maker('Chocolate')        
        
        