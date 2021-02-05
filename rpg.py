import json

def showInstructions():
    # Print a main menu and the commands
    print("""
RPG Game
========

Get to the Garden with a key and a potion.
Avoid the monsters!

You are getting tired; each time you move you lose one health point.

Commands:
    go [north | south | east | west]
    get [item]
""")

# A dictionary linking a room to other room positions
rooms = {
          "Hall" : { "south" : "Kitchen",
                     "east"  : "Dining Room",
                     "item"  : "key"
                   },

          "Kitchen" : { "north" : "Hall",
                        "item"  : "monster"
                      },

          "Dining Room" : { "west"  : "Hall",
                            "south" : "Garden",
                            "item"  : "potion"
                          },

          "Garden" : { "north" : "Dining Room" }
        }


def showStatus():
    # Print the player's current status
    print("---------------------------")
    print(name + " is in the " + currentRoom)
    print("Health : " + str(health))
    # Print the current inventory
    print("Inventory : " + str(inventory))
    # Print an item if there is one
    if "item" in rooms[currentRoom]:
        if rooms[currentRoom]["item"] != "":
            print("You see a " + rooms[currentRoom]["item"])
    print("---------------------------")

try:
    print("Retrieving player details")
    with open("gamedata.json", "r") as f:
        gamedata = json.load(f)
        # Load name
        name = gamedata["playername"]
        # Load inventory
        inventory = gamedata["backpack"]
        # Checks if saved player health was 1
        if gamedata["playerhealth"] <= 1:
            # If so, full health is restored
            health = 5
        else:
            # Otherwise, set health to saved health
            health = gamedata["playerhealth"]
        # Checks if the room is the garden and the player has both the key and potion
        if gamedata["playercurrentRoom"] == "Garden":
            if "key" in inventory:
                if "potion" in inventory:
                    # Reset the game
                    print("You won the last game! Resetting game...")
                    name = None
                    health = 5
                    currentRoom = "Hall"
                    inventory = []
        # Checks if the current room has an item in it
        elif "item" in rooms[gamedata["playercurrentRoom"]]:
            # Checks if the current room has a monster in it
            if rooms[gamedata["playercurrentRoom"]]["item"] == "monster":
                # If so, resets room to Hall
                currentRoom = "Hall"
        else:
            # Otherwise, set room to saved room
            currentRoom = gamedata["playercurrentRoom"]
except FileNotFoundError:
    print("No previous game found. Starting a new game.")
    # Set up the game
    name = None
    health = 5
    currentRoom = "Hall"
    inventory = []

# Remove items in inventory from rooms, before starting
for room, room_dict in rooms.items():
    for key, value in room_dict.items():
        if key == "item":
            if value in inventory:
                rooms[room][key] = ""

# Set up a new game
#name = None
#health = 5
#currentRoom = "Hall"
#inventory = []


# Ask the player their name
if name is None:
    name = input("What is your name, Adventurer? ")
    showInstructions()

# Loop forever
while True:

    showStatus()

    # Get the player's next "move"
    # .split() breaks it up into an list array
    # e.g. typing "go east" would give the list:
    # ["go","east"]
    move = ""
    while move == "":
        move = input(">")

    move = move.lower().split()

    # If they type "go" first
    if move[0] == "go":
        health = health - 1
        # Check that they are allowed wherever they want to go
        if move[1] in rooms[currentRoom]:
            # Set the current room to the new room
            currentRoom = rooms[currentRoom][move[1]]
        # or, if there is no door (link) to the new room
        else:
            print("You can't go that way!")

    # If they type "get" first
    if move[0] == "get" :
        # If the room contains an item, and the item is the one they want to get
        if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]["item"]:
            # Add the item to their inventory
            inventory += [move[1]]
            # Display a helpful message
            print(move[1] + " got!")
            # Delete the item from the room
            del rooms[currentRoom]["item"]
        # Otherwise, if the item isn't there to get
        else:
            # Tell them they can't get it
            print("Can't get " + move[1] + "!")

    # Player loses if they enter a room with a monster
    if "item" in rooms[currentRoom] and "monster" in rooms[currentRoom]["item"]:
        print("A monster has got you ... GAME OVER!")
        break

    if health == 0:
        print("You collapse from exhaustion ... GAME OVER!")
        break

    # Player wins if they get to the garden with a key and a potion
    if currentRoom == "Garden" and "key" in inventory and "potion" in inventory:
        print("You escaped the house ... YOU WIN!")
        break

gamedata = {
        "playername" : name,
        "playerhealth" : health,
        "playercurrentRoom" : currentRoom,
        "backpack" : inventory
    }

with open("gamedata.json", "w") as f:
    json.dump(gamedata, f)