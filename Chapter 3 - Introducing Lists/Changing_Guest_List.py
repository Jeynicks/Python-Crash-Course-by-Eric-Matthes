"""3-5. Changing Guest List: You just heard that one of your guests can’t make the
dinner, so you need to send out a new set of invitations. You’ll have to think of
someone else to invite.
•	 Start with your program from Exercise 3-4. Add a print statement at the
end of your program stating the name of the guest who can’t make it.
•	 Modify your list, replacing the name of the guest who can’t make it with
the name of the new person you are inviting.
•	 Print a second set of invitation messages, one for each person who is still
in your list."""

guest_list = ["Annika", "Robert Downey Jr.", "Andrew Garfield"]

print("Mr. " + str(guest_list[1]) +" can't make it")
guest_list[1] = "Tom Holland"
print()

print(str(guest_list[0]) + ", how about joining me for dinner tonight?")
print("It would mean a lot if you could come to dinner this evening, " + str(guest_list[1]))
print(str(guest_list[2]) + ", let’s catch up over dinner tonight—I’ll save you a seat!")
