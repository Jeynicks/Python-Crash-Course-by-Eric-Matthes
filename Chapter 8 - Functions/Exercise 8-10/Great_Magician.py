"""8-10. Great Magicians: Start with a copy of your program from Exercise 8-9.
Write a function called make_great() 
that modifies the list of magicians by adding the phrase the Great to each magician’s name. 
Call show_magicians() to
see that the list has actually been modified."""

def show_magician(magicians):
    for magician in magicians:
        print(f"Ladies and gentleman, I present to you {magician.title()}\n")

def make_great(magicians): 
       
    for i in range(len(magicians)):
        magicians[i] = f"The Great {magicians[i].title()}"
        
    return magicians  
           

magicians_list = ['Jeynicks', 'Nikaniks', 'oz', 'willie wonka']
magicians_list = make_great(magicians_list) 

show_magician(magicians_list)
