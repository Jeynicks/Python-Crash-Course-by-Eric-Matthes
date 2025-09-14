""". More Guests: You just found a bigger dinner table, so now more space is
available. Think of three more guests to invite to dinner.
•	 Start with your program from Exercise 3-4 or Exercise 3-5. Add a print
statement to the end of your program informing people that you found a
bigger dinner table.
•	 Use insert() to add one new guest to the beginning of your list.
•	 Use insert() to add one new guest to the middle of your list.
•	 Use append() to add one new guest to the end of your list.
•	 Print a new set of invitation messages, one for each person in your list."""

guest_list = ["Annika", "Robert Downey Jr.", "Andrew Garfield"]
guest_list[1] = "Tom Holland"
print("I found a bigger dinner table!")

guest_list.insert(0, "Chris Hemsworth")
guest_list.insert(2, "Scott Lang")
guest_list.append("Max Verstappen")

print("I’m hosting dinner tonight, and I’d be so happy if you could join us, " + str(guest_list))