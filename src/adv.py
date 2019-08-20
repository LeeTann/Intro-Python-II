from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}

items = {
    "sword": Item("sword", "Epic Sword"), 
    "dagger": Item("dagger", "Wooden Dagger"),
    "axe": Item("axe", "Golden Axe")
}

# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

room['narrow'].add_item('sword')
room['narrow'].add_item('dagger')
room['narrow'].add_item('axe')
#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player_name = input("Please enter your name: ")
player = Player(player_name, room['outside'])
print(player)

# Player info
current_player = player.name
current_position = player.current_room

valid_direction = ['n', 's', 'e', 'w', 'q', 'i']
next_move = ""

# sword1 = Sword("Sword", "This is the king of swords", "Legendary", 80)
# room['overlook'].items.append(sword1)

# Write a loop that:
#
while next_move != "q":
    if next_move == 'i':
        if player.inventory == []:
            print("No item in inventory found")
        else:
            print(f"Your inventory: {player.inventory}")

    print(f"{current_position}")
    print(current_position.description)

    if len(current_position.items) > 0:
        item_in_room = current_position.items
        print("You see: ")
        for item in item_in_room:
            print(f"     {item}")
        print("To pick up an item type: take <item-name>...example(take sword)")
        actions = input("What item do you want to take?: ")
        words = actions.strip().lower().split(" ")

        if len(words) >= 2:
            if words[0] == "take":
                if words[1] not in current_position.get_items():
                    print(f"ERROR: take '{words[1]}' not found. please try again.")
                    continue
                else:
                    current_position.del_item(words[1])
                    player.add_item(words[1])
                    player.inventory.append(words[1])
                    print("successfully picked up " + words[1])
            elif words[0] == "drop":
                if words[1] not in player.inventory:
                    print(f"You do not have '{words[1]}' to drop.")
                    continue
                else:
                    current_position.add_item(words[1])
                    player.del_item(words[1])  
                    player.inventory.remove(words[1])
                    print(f"you dropped " + words[1])             
            else:
                print("Error: please input take + item-name")
                continue
        else: 
            print("Error: please input take + item-name")
            

    next_move = input("What's your next move? \nEnter 'n', 's', 'e', or 'w' to move, 'i' for inventory or Enter 'q' to quit: ")

    try:
        if next_move not in valid_direction:
            print("Invalid Input!")
        elif next_move in valid_direction:
            if next_move == "n":
                if not current_position.n_to == None:
                    current_position = current_position.n_to
                else:
                    print("Dead End.")
            if next_move == 's':
                if not current_position.s_to == None:
                    current_position = current_position.s_to
                else:
                    print("Dead End.")
            if next_move == 'e':
                if not current_position.e_to == None:
                    current_position = current_position.e_to
                else:
                    print("Dead End.")
            if next_move == 'w':
                if not current_position.w_to == None:
                    current_position = current_position.w_to
                else:
                    print("Dead End.")
        else: 
            print("No room that way bro")
    except:
        print("Incorrect route. Please choose another.")

print("Game over. You quit!!")
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
