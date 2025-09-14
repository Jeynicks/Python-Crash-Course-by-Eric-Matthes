"""7-5. Movie Tickets: A movie theater charges different ticket prices depending on
a person’s age. If a person is under the age of 3, the ticket is free; if they are
between 3 and 12, the ticket is $10; and if they are over age 12, the ticket is
$15. Write a loop in which you ask users their age, and then tell them the cost
of their movie ticket."""

prompt = "How old are you?\n"
prompt += "Enter 'quit' if you want to exit. "

respond = ""

while respond != 'quit':
    respond = input(prompt)
    age = int(respond)
    
    if age < 3:
        print("Ticket is free")
    elif age >= 3 and age <= 12:
        print("Ticket is $10")
    else:
        print("Ticket is $15")        

