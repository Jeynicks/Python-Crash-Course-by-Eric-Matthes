"""8-8. User Albums: Start with your program from Exercise 8-7. Write a while
loop that allows users to enter an album’s artist and title. Once you have that
information, call make_album() with the user’s input and print the dictionary
that’s created. Be sure to include a quit value in the while loop."""

def make_album(artist_name, album_title):
    return {artist_name: album_title}


artist_name = ''
album_title = ''

respond = ''

album_list = []
while respond != 'quit':
    artist_name = input('Enter artist name: ')
    album_title = input('Enter album title: ')
    
    album_list.append(make_album(artist_name, album_title))
    
    respond = input("Enter 'quit' if you want to exit program.: ")
    respond.lower()

print(album_list)    