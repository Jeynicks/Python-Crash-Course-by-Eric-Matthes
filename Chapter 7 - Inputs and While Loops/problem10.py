"""7-10. Dream Vacation: Write a program that polls users about their dream
vacation. Write a prompt similar to If you could visit one place in the world,
where would you go? Include a block of code that prints the results of the poll."""

poll_result = []

active_poll = True

prompt = "If you could go to your dream vacation for a day, where would it be? \n"
prompt += "Enter 'quit' to exit: "

while active_poll:
    response = input(prompt)
    
    if response == 'quit':
        active_poll = False
    else:
        poll_result.append(response)    
        
print(f"Poll Result: {poll_result}")        
        