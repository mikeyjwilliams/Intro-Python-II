#!/usr/bin/env python3

from os import system, name
import time
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


def intro_message():
    print('''****************************''')
    print('''    Text Adventure Game     ''')
    print('''****************************''')


def user_controls():
    directions = { 'n': 'North', 's': 'South', 'e': 'East', 'w': 'West', 'q': 'quit' }
    
    print('Please select a direction to go in.')
    for key, val in directions.items():
        if key != 'q':
            print(f'enter [{key}] key for {val} direction')
        else:
            print(f'enter [{key}] key for {val} quit')
    



def direction_layout(choice):
    directions = { 'n': 'North', 's': 'South', 'e': 'East', 'w': 'West', 'q': 'quit' }
    if choice == 's' or choice == 'n' or choice == 'e' or choice == 'w':
        
        if getattr(player.current_room, f'{choice}_to') is not None:
            print(f'{player.name} moved {directions[choice]}')
            player.current_room = getattr(player.current_room, f'{choice}_to')
            return player
        else:
            print('that direction is blocked, please choose another....')
            return player
        
        
# define our clear function 
def clear(): 
  
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear')
    

intro_message()
name = input('please enter your name ')
player = Player(name, room['outside'])

# print(room['outside'].n_to)
while True:
    # print('N ', player.room_current())
   
    print(player)
    print()
    user_controls()
    print()
    choice = input('Please choose a direction....')
    print(choice)
    if choice == 'q':
        clear()
        print('Thank you for playing....')
        time.sleep(3)
        print('see you next time')
        time.sleep(2)
        print('goodbye')
        time.sleep(1)
        print('\' Remember: reality is an illusion. The universe is a hologram. Buy gold. Bye!')
        break
     
    
    player = direction_layout(choice)
    
    

#
# Main
#

# Make a new player object that is currently in the 'outside' room.


# Write a loop that:
#
# * Prints the current room name


# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.


    
    
        
    