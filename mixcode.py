# Launch date code worked. 
import datetime
print ("Hello Sneha")
launch_date = datetime.date(1991, 10, 8)
print(launch_date)

# But this code isn't working saying that "Raw_input" is not defined. Replicated it from Module 2 part 4 "If Statements"
#input = raw_input("Please enter a test string:")

#if len(input) < 8:
#   print("Your string is too short,")
#   print("Please enter a string with at least 6 character.")



# But this code works when I put the input after the variable. I am not sure how the above code worked in the video from the module.
raw_input = input("Please enter an integer: ")
number = int(raw_input)
if number % 2 == 0:
    print("Your number is even.")
else: 
    print("Your number is odd.")
