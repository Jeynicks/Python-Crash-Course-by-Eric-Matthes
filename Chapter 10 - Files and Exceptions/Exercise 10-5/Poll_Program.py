"""10-5. Programming Poll: Write a while loop that asks people why they like
programming. Each time someone enters a reason, add their reason to a file
that stores all the responses"""

file_path = 'Chapter 10 - Files and Exceptions\\Exercise 10-5\\response.txt'

with open(file_path, 'a') as responses:
    
    while True:
        reason = input('Why do you love programming?\nEnter "q" to quit: ')
        print()
        if reason == 'q':
            break
        responses.write(f"{reason}\n")
