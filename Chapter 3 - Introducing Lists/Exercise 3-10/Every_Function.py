"""3-10. Every Function: Think of something you could store in a list. For example,
you could make a list of mountains, rivers, countries, cities, languages, or anything else you’d like. Write a program that creates a list containing these items
and then uses each function introduced in this chapter at least once"""

the_list = ["Greninja"]
print("My List: "+str(the_list))
print()

the_list.append("Lua")
print("Adding my first programming language: " + str(the_list))
print()

the_list.insert(0, 36)
print("Inserting my favorite number to the list: " + str(the_list))
print()

the_list.reverse()
print("My List in reverse: " + str(the_list))
print()

sorted(str(the_list))
print("My List sorted alphabetically: " + str(the_list))
print()

sorted(str(the_list), reverse= True)
print("My list in reverse alphabetical order: " + str(the_list))
print()

favorite_num = the_list.pop()
print("If I'll have a jersey number this is my number: " + str(favorite_num))
print()

the_list.remove("Greninja")
print("Removing Greninja from my list: " + str(the_list))
print()

del the_list[0]
print("Deleting My List: " + str(the_list))
 
