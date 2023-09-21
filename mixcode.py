import datetime
print ("Hello Sneha")
launch_date = datetime.date(1991, 10, 8)
print(launch_date)
# Launch date code worked. 

#input = raw_input("Please enter a test string:")

#if len(input) < 8:
#   print("Your string is too short,")
#   print("Please enter a string with at least 6 character.")
# But this code isn't working. Replicated it from Module 2 part 4 "If Statements"

input = raw_input("Please enter an integer: ")
number = int(input)
if number % 2 == 0:
    print("Your number is even.")
else: 
    print("Your number is odd.")
# This code is also giving same error. Can't figure out what is wrong.