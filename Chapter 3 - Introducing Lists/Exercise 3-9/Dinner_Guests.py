"""3-9. Dinner Guests: Working with one of the programs from Exercises 3-4
through 3-7 (page 46), use len() to print a message indicating the number
of people you are inviting to dinner"""

guest_list = ["Annika", "Robert Downey Jr.", "Andrew Garfield"]
guest_list[1] = "Tom Holland"
guest_list.insert(0, "Chris Hemsworth")
guest_list.insert(2, "Scott Lang")
guest_list.append("Max Verstappen")

print("I am inviting "+ str(len(guest_list)) + " people")