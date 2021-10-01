class Building_material:
    def __init__(self, name, use, hue, brightness, wood):
        self.name = name
        self.use = use
        self.hue = hue
        self.brightness = brightness
        self.wood = wood

cobblestone = Building_material("cobblestone", "WR", "greyscale", "mid", False)
oak = Building_material("oak", "WFR", "yellow", "mid", True)
stone_bricks = Building_material("stone bricks", "W", "greyscale", "mid", False)
sandstone = Building_material("sandstone", "F", "yellow", "light", False)
birch = Building_material("birch", "WF", "yellow", "light", True)
spruce = Building_material("spruce", "WFR", "orange", "mid-dark", True)
jungle = Building_material("jungle wood", "WF", "orange", "mid", True)
dark_oak = Building_material("dark oak", "WFR", "orange", "dark", True)
acacia = Building_material("acacia", "W", "orange", "mid", True)
smooth_sandstone = Building_material("smooth sandstone", "W", "yellow", "light", False)
cut_sandstone = Building_material("cut sandstone", "W", "yellow", "light", False)
bricks = Building_material("bricks", "W", "orange", "mid", False)
andesite = Building_material("andesite", "F", "greyscale", "mid-light", False)
diorite = Building_material("diorite", "F", "greyscale", "light", False)
granite = Building_material("granite", "F", "orange", "mid", False)
nether_bricks = Building_material("nether bricks", "W", "red", "dark", False)
red_nether_bricks = Building_material("red nether bricks", "W", "red", "mid-dark", False)
warped_wood = Building_material("warped wood", "WF", "cyan", "mid", True)
crimson_wood = Building_material("crimson planks", "WFR", "magenta", "mid", True)
blackstone = Building_material("blackstone", "WFR", "greyscale", "dark", False)
deepslate = Building_material("deepslate", "WFR", "greyscale", "mid-dark", False)
copper = Building_material("copper", "WFR", "orange", "mid", False)
prismarine = Building_material("prismarine", "W", "cyan", "mid-light", False)
prismarine_bricks = Building_material("prismarine bricks", "W", "cyan", "mid", False)
dark_prismarine = Building_material("dark prismarine", "FR", "green", "dark", False)
endstone_bricks = Building_material("endstone bricks", "W", "yellow", "light", False)
purpur = Building_material("purpur", "WFR", "purple", "mid-light", False)
quartz = Building_material("quartz", "WF", "greyscale", "light", False)
white_concrete = Building_material("white concrete", "W", "greyscale", "light", False)
light_grey_concrete = Building_material("light grey concrete", "W", "greyscale", "mid-light", False)
grey_concrete = Building_material("grey concrete", "W", "greyscale", "mid-dark", False)
black_concrete = Building_material("black concrete", "W", "greyscale", "dark", False)
pink_concrete = Building_material("pink concrete", "W", "red", "light", False)
red_concrete = Building_material("red concrete", "W", "red", "mid", False)
orange_concrete = Building_material("orange concrete", "W", "orange", "mid-light", False)
brown_concrete = Building_material("brown concrete", "W", "orange", "mid-dark", False)
yellow_concrete = Building_material("yellow concrete", "W", "yellow", "light", False)
lime_concrete = Building_material("lime concrete", "W", "green", "light", False)
green_concrete = Building_material("green concrete", "W", "green", "mid-dark", False)
cyan_concrete = Building_material("cyan concrete", "W", "cyan", "mid-dark", False)
light_blue_concrete = Building_material("light blue concrete", "W", "blue", "light", False)
blue_concrete = Building_material("blue concrete", "W", "blue", "mid", False)
magenta_concrete = Building_material("magenta concrete", "W", "magenta", "mid-light", False)
purple_concrete = Building_material("purple concrete", "W", "purple", "dark", False)
white_wool = Building_material("white wool", "F", "greyscale", "light", False)
light_grey_wool = Building_material("light grey wool", "F", "greyscale", "mid-light", False)
grey_wool = Building_material("grey wool", "F", "greyscale", "mid-dark", False)
black_wool = Building_material("black wool", "F", "greyscale", "dark", False)
pink_wool = Building_material("pink wool", "F", "red", "light", False)
red_wool = Building_material("red wool", "F", "red", "mid-light", False)
orange_wool = Building_material("orange wool", "F", "orange", "mid-light", False)
brown_wool = Building_material("brown wool", "F", "orange", "mid-dark", False)
yellow_wool = Building_material("yellow wool", "F", "yellow", "light", False)
lime_wool = Building_material("lime wool", "F", "green", "light", False)
green_wool = Building_material("green wool", "F", "green", "mid", False)
cyan_wool = Building_material("cyan wool", "F", "cyan", "mid-dark", False)
light_blue_wool = Building_material("light blue wool", "F", "blue", "light", False)
blue_wool = Building_material("blue wool", "F", "blue", "mid", False)
magenta_wool = Building_material("magenta wool", "F", "magenta", "light", False)
purple_wool = Building_material("purple wool", "F", "purple", "mid-dark", False)

building_blocks = [cobblestone, stone_bricks, sandstone, blackstone, oak, spruce, birch, dark_oak, acacia, nether_bricks, red_nether_bricks, prismarine, prismarine_bricks, dark_prismarine, warped_wood, crimson_wood, quartz, deepslate, copper, cut_sandstone, smooth_sandstone, purpur, endstone_bricks, white_concrete, white_wool, light_blue_concrete, light_blue_wool, light_grey_concrete, light_grey_wool, green_concrete, green_wool, grey_concrete, grey_wool, granite, andesite, diorite, black_concrete, black_wool, pink_concrete, pink_wool, red_wool, red_concrete, orange_concrete, orange_wool, yellow_concrete, yellow_wool, lime_concrete, lime_wool, cyan_concrete, cyan_wool, blue_concrete, blue_wool, magenta_concrete, magenta_wool, purple_concrete, purple_wool, bricks]

#function for choosing what to do after finishing with an app
def continue_choice(origin_screen):
    choice = input("Do you want to continue with this (A), return to the main menu (B) or quit(C)?")
    if choice == "B":
        menu()
    elif choice == "C":
        quit()
    elif choice == "A":
        if origin_screen == "A":
            area()
        elif origin_screen == "B":
            build()
    else:
        print("Sorry I didn't understand that.")
        continue_choice(origin_screen)


#the area math app
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

    continue_choice("A")

def search(block):
    selection = ""
    for i in building_blocks:
        if block == i.name:
            selection = i
    return selection

def where(block):
    WFR = ""
    if block.use == "W":
        WFR = "walls."
    elif block.use == "F":
        if block.wood == True:
            WFR = "floors (especially stripped wood)."
        else: WFR = "floors."
    elif block.use == "R":
        WFR = "roofs (slabs and stairs)."
    elif block.use == "WF":
        if block.wood == True:
            WFR = "walls and floors (especially stripped wood)"
        else:
            WFR = "walls and floors."
    elif block.use == "WR":
        WFR = "walls and roofs (slabs and stairs)."
    elif block.use == "FR":
        if block.wood == True:
            WFR = "floors (especially stripped wood) and roofs (slabs and stairs)."
        else:
            WFR = "floors and roofs (slabs and stairs)."
    elif block.use == "WFR":
        if block.wood == True:
            WFR = "walls, floors (especially stripped wood) and roofs (slabs and stairs)."
        else:
            WFR = "walls, floors and roofs (slabs and stairs)."
    else:
        print("Error.  Data missing or unrecognised.")
    print("Useful for " + WFR)


def compare(block):
    chosen_block = search(block)
    print(chosen_block.name)
    where(chosen_block)
    
#compare building blocks app
def build():
    block = input("Pick a building block in Minecraft: ")
    compare(block)
    continue_choice("B")

#details about blocks and items
def details():
    print("lets get some information about items and blocks!!")
    menu()

#details about mobs
def mobs():
    print("lets get some information about mobs!!!")
    menu()

#minecraft progression
def progress():
    print("what can you do when?  Welcome to Minecraft progression.")
    menu()

#timeline of minecraft development
def timeline():
    print("this is the story of Minecraft's development and what got added when.")
    menu()

#quit function
def quit():
    print("bye bye")

#error function for unrecognised menu input
def error():
    print("Sorry I didn't recognise that input.")
    print("Please choose again")
    menu()

#select menu options
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


#the menu text, explaining the different apps
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

#introductory message
print("Welcome to Everything Minecraft")
menu()

