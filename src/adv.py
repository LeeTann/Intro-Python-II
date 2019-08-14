from room import Room
from player import Player

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


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player_name = input("Please enter your name: ")
player1 = Player(player_name, room['outside'])
# print(player1)

# Player info
current_player = player1.name
current_position = player1.current_room
next_move = ""

# Write a loop that:
#
while next_move != "q":
    print(f"Hi Lee, {current_position}")
    print(current_position.description)
    
    next_move = input("What's your next move? \nEnter 'n', 's', 'e', or 'w' to move or Enter 'q' to quit: ")

    try:
        if next_move == "n":
            current_position = current_position.n_to
        if next_move == 's':
            current_position = current_position.s_to
        if next_move == 'e':
            current_position = current_position.e_to
        if next_move == 'w':
            current_position = current_position.w_to
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
