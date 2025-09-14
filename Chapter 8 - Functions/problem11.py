"""8-11. Unchanged Magicians: Start with your work from Exercise 8-10. Call the
function make_great() with a copy of the list of magicians’ names. Because the
original list will be unchanged, return the new list and store it in a separate list.
Call show_magicians() with each list to show that you have one list of the original names 
and one list with the Great added to each magician’s name"""

def show_magician(magicians):
    for magician in magicians:
        print(f"Ladies and gentleman, I present to you {magician.title()}\n")

def make_great(magicians): 
       
    for i in range(len(magicians)):
        magicians[i] = f"The Great {magicians[i].title()}"
        
    return magicians       

magicians_list = ['Jeynicks', 'Nikaniks', 'oz', 'willie wonka']
great_magicians = make_great(magicians_list[:]) 

print("Original List")
show_magician(magicians_list)
print('The Great List')
show_magician(great_magicians)


