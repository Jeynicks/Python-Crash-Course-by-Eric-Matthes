"""3-11. Intentional Error: If you haven’t received an index error in one of your
programs yet, try to make one happen. Change an index in one of your programs to produce an index error. Make sure you correct the error before closing the program.
"""
guest_list = ["Annika", "Robert Downey Jr.", "Andrew Garfield"]
guest_list[1] = "Tom Holland"
guest_list.insert(0, "Chris Hemsworth")
guest_list.insert(2, "Scott Lang")
guest_list.append("Max Verstappen")

print("Hello " + str(guest_list[7]))