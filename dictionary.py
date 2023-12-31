# Below are few functions we have.
def do_one(x):
    print("one: x*1 = ", x*1)

def do_two(x):
    print("two: x*2 = ", x*2)

def do_three(x):
    print("three: x*3 = ", x*3)

def do_default(x):
    print("default: x = ", x)


#This is normal elif statement but there are too many elifs and we can avoid that using Dictionary.
x = 4

if x == 1:
    do_one(x)
elif x == 2:
    do_two(x)
elif x == 3:
    do_three(x)
else:
    do_default(x)

# This is how we can use Dictionary where we can put options as key and functions as value to make the code shorter.
actions = {1: do_one, 2: do_two, 3: do_three}

action = actions.get(x, do_default)
action(x)