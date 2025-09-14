"""3-7. Shrinking Guest List: You just found out that your new dinner table won’t
arrive in time for the dinner, and you have space for only two guests.
•	 Start with your program from Exercise 3-6. Add a new line that prints a
message saying that you can invite only two people for dinner.
•	 Use pop() to remove guests from your list one at a time until only two
names remain in your list. Each time you pop a name from your list, print
a message to that person letting them know you’re sorry you can’t invite
them to dinner.
•	 Print a message to each of the two people still on your list, letting them
know they’re still invited.
•	 Use del to remove the last two names from your list, so you have an empty
list. Print your list to make sure you actually have an empty list at the end
of your program."""

guest_list = ["Annika", "Robert Downey Jr.", "Andrew Garfield"]
guest_list[1] = "Tom Holland"
guest_list.insert(0, "Chris Hemsworth")
guest_list.insert(2, "Scott Lang")
guest_list.append("Max Verstappen")

uninvite_guest = []
uninvite_guest.append(guest_list.pop())
uninvite_guest.append(guest_list.pop())
uninvite_guest.append(guest_list.pop())
uninvite_guest.append(guest_list.pop())

print("Hi " + str(uninvite_guest[0]) +", I’m really sorry, but my dinner table can only seat two guests tonight. I’ll definitely make sure to invite you next time.")
print(str(uninvite_guest[1]) + ", I wish I could have everyone over, but space is tight this evening. Let’s plan another dinner soon just for us.")
print("Hey " + str(uninvite_guest[2]) + ", I wanted to let you know that I can only host two guests at dinner tonight, so sadly I can’t include you this time. I’d love to make it up to you another day.")
print(str(uninvite_guest[3]) + ", thank you for being open to joining, but my table is really limited tonight. I’ll be sure to save you a seat at the next dinner.")

print()

print("Hi "+ str(guest_list[1]) + ", just confirming—you’re still invited to dinner tonight. Looking forward to having you at the table!")
print(str(guest_list[0]) + ", you’re one of the two special guests tonight—I can’t wait to share dinner with you.")
del guest_list[0]
del guest_list[0]
print()


print("Empty Guest List: " + str(guest_list))