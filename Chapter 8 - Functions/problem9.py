"""8-9. Magicians: Make a list of magician’s names. Pass the list to a function
called show_magicians(), which prints the name of each magician in the list."""

def show_magician(magicians):
    for magician in magicians:
        print(f"Ladies and gentleman, I present to you {magician.title()}\n")
        

magicians_list = ['Jeynicks', 'Nikaniks', 'oz', 'willie wonka']
show_magician(magicians_list)        