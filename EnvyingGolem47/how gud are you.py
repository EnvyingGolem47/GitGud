import random

user = input("Username:")
roll = random.randint(0, 20)

if(roll <= 20):
    print("Hey, your pretty good!"+" @"+user)
    d = input(": ")
else:
    print("Git GUD!"+" @"+user)
    d = input(": ")