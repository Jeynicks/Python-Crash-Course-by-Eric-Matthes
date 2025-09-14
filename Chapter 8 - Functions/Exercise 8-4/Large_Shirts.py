"""8-4. Large Shirts: Modify the make_shirt() function so that shirts are large
by default with a message that reads I love Python. Make a large shirt and a
medium shirt with the default message, and a shirt of any size with a different
message."""

def make_shirt(message= 'I love Python', size= 'large'):
    
    if size == 'large':
        print(f"Your T-Shirt\n"+
          f"Size: {size}\n"+
          f"Text: I love Python")
          
    elif size == 'medium':
        print(f"Your T-Shirt\n"+
          f"Size: {size}\n"+
          f"Text: I love programming") 
           
    else:
        print(f"Your T-Shirt\n"+
          f"Size: {size}\n"+
          f"Text: {message}")      
        

make_shirt()
make_shirt(size= 'medium')
make_shirt(message= 'Hello World', size= 'small')
