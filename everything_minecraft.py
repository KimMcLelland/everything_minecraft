def area():
    print("Welcome to the area math calculator")
    print("first tell me how many blocks by how many blocks horizontally?")
    width = int(input("1st horizontal direction: "))
    length = int(input("2nd horizontal direction: "))
    height = int(input("Now how many blocks high is your building? "))
    floors = int(input("How many floors? "))
    doors = int(input("How many doors? "))
    windows = int(input("How many windows? "))
    windowWidth = int(input("How wide are those windows? "))
    windowHeight = int(input("How high are those windows? "))
    widthWalls = (width - 1) * 2
    lengthWalls = (length - 1) * 2
    doorSize = doors * 2
    windowSize = windowWidth * windowHeight * windows
    floorArea = (width - 2) * (length - 2)


    print("The amount of blocks you'll need for the external walls are: ")
    print(((widthWalls + lengthWalls) * height) - doorSize - windowSize)
    print("The amount of blocks you'll need for the floors are: ")
    print(floorArea * floors)
    print("The amount of blocks you'll likely need for the roof are: ")
    print((width + 2) * (length + 2))

    menu()

def build():
    print("lets compare some building blocks!")
    menu()

def details():
    print("lets get some information about items and blocks!!")
    menu()

def mobs():
    print("lets get some information about mobs!!!")
    menu()

def progress():
    print("what can you do when?  Welcome to Minecraft progression.")
    menu()

def timeline():
    print("this is the story of Minecraft's development and what got added when.")
    menu()

def quit():
    print("bye bye")

def error():
    print("Sorry I didn't recognise that input.")
    print("Please choose again")
    menu()

def select():
    choice = input("What function do you want to use? ")
    if choice == "A":
        area()
    elif choice == "B":
        build()
    elif choice == "D":
        details()
    elif choice == "M":
        mobs()
    elif choice == "P":
        progress()
    elif choice == "T":
        timeline()
    elif choice == "Q":
        quit()
    else:
        error()


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

