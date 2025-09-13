"""5-9. No Users: Add an if test to hello_admin.py to make sure the list of users is
not empty.
•	 If the list is empty, print the message We need to find some users!
•	 Remove all of the usernames from your list, and make sure the correct
message is printed."""

#users = ['Jeynicks', 'Nikaniks', 'noobmaster69', 'Faker', 'Tenz', 'admin']
users = []

if users:
    for user in users:
        if user == 'admin':
            print("Hello admin, would you like to see a status report")
        else:
            print(f"Hello {user}, Thank you for logging in again.") 
else:
    print("We need to find some users!")               
