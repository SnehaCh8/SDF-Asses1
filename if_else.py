# Its interesting ti know that python knows the mathematical signs like plus, minus, greater, smaller etc.
if 2 > 3:
    print("This is true")
else:
    print("No this is not true")

# Testing more if else statements - Getting the error that No is not defined as soon as we get to that part.
# So a great learning is that the word No should be in quote and that is what I was missing. As soon as I change the No to "No" it worked fine.
fav_food = input("What is your Fav food\n")
if fav_food == "Pasta":
    spices = input("Is it cooked with enough spices?\n")
    if spices == "No":
        print("This is not yummy")
        exit()
    else:
        print("This is Yummy")

