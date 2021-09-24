def area():
    print("lets calculate some numbers")
    select()

def build():
    print("lets compare some building blocks!")
    select()

def details():
    print("lets get some information about items and blocks!!")
    select()

def mobs():
    print("lets get some information about mobs!!!")
    select()

def progress():
    print("what can you do when?  Welcome to Minecraft progression.")
    select()

def timeline():
    print("this is the story of Minecraft's development and what got added when.")
    select()

def quit():
    print("bye bye")

def select():
    choice = input("What function do you want to use?")
    if choice == "A":
        area()
    if choice == "B":
        build()
    if choice == "D":
        details()
    if choice == "M":
        mobs()
    if choice == "P":
        progress()
    if choice == "T":
        timeline()
    if choice == "Q":
        quit()
    else:
        print("Sorry I didn't recognise that input.")
        print("Please choose again")
        menu()


def menu():
    print("You can do the following:")
    print("calculate amount of materials for a build (type 'A' for Area Math)")
    print("Search for compatible materials to use with a specific building block (type 'B' for Build)")
    print("Search any material or item for details on how to get it and what you can make with it (type 'D' for details)")
    print("Search any mob for information on its environment, behaviour and what it drops when killed (type 'M' for Mob")
    print("A look at the different stages of progression in the game (type 'P' for progress)")
    print("Look at a timeline of development in Minecraft (type 'T' for timeline)")
    print("Or of course you could quit (Q)")
    select()

print("Welcome to Everything Minecraft")
menu()

