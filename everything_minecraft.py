class Building_material:
    def __init__(self, name, use, hue, brightness, wood):
        self.name = name
        self.use = use
        self.hue = hue
        self.brightness = brightness
        self.wood = wood

cobblestone = Building_material("cobblestone", "WR", 0, 3, False)
oak = Building_material("oak", "WFR", 3, 3, True)
stone_bricks = Building_material("stone bricks", "W", 0, 3, False)
sandstone = Building_material("sandstone", "F", 3, 5, False)
birch = Building_material("birch", "WF", 3, 5, True)
spruce = Building_material("spruce", "WFR", 2, 2, True)
jungle = Building_material("jungle wood", "WF", 2, 3, True)
dark_oak = Building_material("dark oak", "WFR", 2, 1, True)
acacia = Building_material("acacia", "W", 2, 3, True)
smooth_sandstone = Building_material("smooth sandstone", "W", 3, 5, False)
cut_sandstone = Building_material("cut sandstone", "W", 3, 5, False)
bricks = Building_material("bricks", "W", 2, 3, False)
andesite = Building_material("andesite", "F", 0, 4, False)
diorite = Building_material("diorite", "F", 0, 5, False)
granite = Building_material("granite", "F", 2, 3, False)
nether_bricks = Building_material("nether bricks", "W", 1, 1, False)
red_nether_bricks = Building_material("red nether bricks", "W", 1, 2, False)
warped_wood = Building_material("warped wood", "WF", 5, 3, True)
crimson_wood = Building_material("crimson planks", "WFR", 8, 3, True)
blackstone = Building_material("blackstone", "WFR", 0, 1, False)
deepslate = Building_material("deepslate", "WFR", 0, 2, False)
copper = Building_material("copper", "WFR", 2, 3, False)
prismarine = Building_material("prismarine", "W", 5, 4, False)
prismarine_bricks = Building_material("prismarine bricks", "W", 5, 3, False)
dark_prismarine = Building_material("dark prismarine", "FR", 4, 1, False)
endstone_bricks = Building_material("endstone bricks", "W", 3, 5, False)
purpur = Building_material("purpur", "WFR", 7, 4, False)
quartz = Building_material("quartz", "WF", 0, 5, False)
white_concrete = Building_material("white concrete", "W", 0, 5, False)
light_grey_concrete = Building_material("light grey concrete", "W", 0, 4, False)
grey_concrete = Building_material("grey concrete", "W", 0, 2, False)
black_concrete = Building_material("black concrete", "W", 0, 1, False)
pink_concrete = Building_material("pink concrete", "W", 1, 5, False)
red_concrete = Building_material("red concrete", "W", 1, 3, False)
orange_concrete = Building_material("orange concrete", "W", 2, 4, False)
brown_concrete = Building_material("brown concrete", "W", 2, 2, False)
yellow_concrete = Building_material("yellow concrete", "W", 3, 5, False)
lime_concrete = Building_material("lime concrete", "W", 4, 5, False)
green_concrete = Building_material("green concrete", "W", 4, 2, False)
cyan_concrete = Building_material("cyan concrete", "W", 5, 2, False)
light_blue_concrete = Building_material("light blue concrete", "W", 6, 5, False)
blue_concrete = Building_material("blue concrete", "W", 6, 3, False)
magenta_concrete = Building_material("magenta concrete", "W", 8, 4, False)
purple_concrete = Building_material("purple concrete", "W", 7, 1, False)
white_wool = Building_material("white wool", "F", 0, 5, False)
light_grey_wool = Building_material("light grey wool", "F", 0, 4, False)
grey_wool = Building_material("grey wool", "F", 0, 2, False)
black_wool = Building_material("black wool", "F", 0, 1, False)
pink_wool = Building_material("pink wool", "F", 1, 5, False)
red_wool = Building_material("red wool", "F", 1, 4, False)
orange_wool = Building_material("orange wool", "F", 2, 4, False)
brown_wool = Building_material("brown wool", "F", 2, 2, False)
yellow_wool = Building_material("yellow wool", "F", 3, 5, False)
lime_wool = Building_material("lime wool", "F", 4, 5, False)
green_wool = Building_material("green wool", "F", 4, 3, False)
cyan_wool = Building_material("cyan wool", "F", 5, 2, False)
light_blue_wool = Building_material("light blue wool", "F", 6, 5, False)
blue_wool = Building_material("blue wool", "F", 6, 3, False)
magenta_wool = Building_material("magenta wool", "F", 8, 5, False)
purple_wool = Building_material("purple wool", "F", 7, 2, False)

building_blocks = [cobblestone, stone_bricks, sandstone, blackstone, oak, spruce, birch, dark_oak, acacia, nether_bricks, red_nether_bricks, prismarine, prismarine_bricks, dark_prismarine, warped_wood, crimson_wood, quartz, deepslate, copper, cut_sandstone, smooth_sandstone, purpur, endstone_bricks, white_concrete, white_wool, light_blue_concrete, light_blue_wool, light_grey_concrete, light_grey_wool, green_concrete, green_wool, grey_concrete, grey_wool, granite, andesite, diorite, black_concrete, black_wool, pink_concrete, pink_wool, red_wool, red_concrete, orange_concrete, orange_wool, yellow_concrete, yellow_wool, lime_concrete, lime_wool, cyan_concrete, cyan_wool, blue_concrete, blue_wool, magenta_concrete, magenta_wool, purple_concrete, purple_wool, bricks]

#function for choosing what to do after finishing with an app
def continue_choice(origin_screen):
    decision = input("Do you want to continue with this (A), return to the main menu (B) or quit(C)?")
    if decision == "B":
        menu()
    elif decision == "C":
        quit()
    elif decision == "A":
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

def hue_test(hue1, hue2):
    huematch = None
    if hue1 == 0 and hue2 != 0:
        huematch = True
    elif hue1 != 0 and hue2 == 0:
        huematch = True
    elif hue1 == 0 and hue2 == 0:
        huematch = False
    elif hue1 == 1:
        if hue2 > 3 and hue2 < 7:
            huematch = True
        else:
            huematch = False
    elif hue1 == 2:
        if hue2 > 4 and hue2 < 8:
            huematch = True
        else:
            huematch = False
    elif hue1 == 3 and hue2 > 5:
        huematch = True
    elif hue1 == 4:
        if hue2 > 6  or hue2 < 2:
            huematch = True
        else:
            huematch = False
    elif hue1 == 5:
        if hue2 > 7 or hue2 < 3:
            huematch = True
        else:
            huematch = False
    elif hue1 == 6 and hue2 < 4:
        huematch = True
    elif hue1 == 7:
        if hue2 > 1 and hue2 < 5:
            huematch = True
        else:
            huematch = False
    elif hue1 == 8:
        if hue2 > 2 and hue2 < 6:
            huematch = True
        else:
            huematch = False
    else:
        huematch = False
    return huematch

def brightness_test(brightness1, brightness2):
    brightmatch = None
    if brightness1 > 3 and brightness2 < 3:
        brightmatch = True
    elif brightness1 < 3 and brightness2 > 3:
        brightmatch = True
    elif brightness1 == 3 or brightness2 == 3:
        brightmatch = True
    else:
        brightmatch = False
    return brightmatch

def walls(block):
    print("\u0332".join("Walls"))
    print("For floors and roof use:")
    for i in building_blocks:
        if i.use != "W":
            hue_match = hue_test(block.hue, i.hue)
            brightness_match = brightness_test(block.brightness, i.brightness)
            if hue_match == True and brightness_match == True:
                print(i.name)
    print("")
    

def floor(block):
    print("\u0332".join("Floor"))
    print("For walls use:")
    for i in building_blocks:
        if i.use == "W" or i.use == "WF" or i.use == "WR" or i.use == "WFR":
            hue_match = hue_test(block.hue, i.hue)
            brightness_match = brightness_test(block.brightness, i.brightness)
            if hue_match == True and brightness_match == True:
                print(i.name)
    print("")

def roof(block):
    print("\u0332".join("Roof"))
    print("For walls use:")
    for i in building_blocks:
        if i.use == "W" or i.use == "WF" or i.use == "WR" or i.use == "WFR":
            hue_match = hue_test(block.hue, i.hue)
            brightness_match = brightness_test(block.brightness, i.brightness)
            if hue_match == True and brightness_match == True:
                print(i.name)
    print("")
    print("")


def where(block):
    WFR = ""
    if block.use == "W":
        WFR = "walls."
        walls(block)
    elif block.use == "F":
        if block.wood == True:
            WFR = "floors (especially stripped wood)."
        else: WFR = "floors."
        floor(block)
    elif block.use == "R":
        WFR = "roofs (slabs and stairs)."
        roof(block)
    elif block.use == "WF":
        if block.wood == True:
            WFR = "walls and floors (especially stripped wood)"
        else:
            WFR = "walls and floors."
        walls(block)
        floor(block)
    elif block.use == "WR":
        WFR = "walls and roofs (slabs and stairs)."
        walls(block)
        roof(block)
    elif block.use == "FR":
        if block.wood == True:
            WFR = "floors (especially stripped wood) and roofs (slabs and stairs)."
        else:
            WFR = "floors and roofs (slabs and stairs)."
        floor(block)
        roof(block)
    elif block.use == "WFR":
        if block.wood == True:
            WFR = "walls, floors (especially stripped wood) and roofs (slabs and stairs)."
        else:
            WFR = "walls, floors and roofs (slabs and stairs)."
        walls(block)
        floor(block)
        roof(block)
    else:
        print("Error.  Data missing or unrecognised.")
    print("Useful for " + WFR)



def compare(block):
    chosen_block = search(block)
    if chosen_block == "":
        print("Sorry but that block is unrecognised.  It either doesn't exist, hasn't been added to this app, or was entered incorrectly.  Please pick another block.")
        build()
    else:
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

