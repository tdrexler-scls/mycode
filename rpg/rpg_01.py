#!/usr/bin/env python3
"""RPG project"""

def create_rooms():
    
    room_list = [


    map = {
            'Hall' : { 
                'south': 'Kitchen',
                'east': 'Dining Room',
                'item': 'key'
                },

            'Kitchen' : {
                'north': 'Hall',
                'item': 'monster'
                },

            'Dining Room' : {
                'west': 'Hall',
                'south': 'Garden',
                'item': 'potion',
                'north': 'Pantry'
                },

            'Garden' : {
                'north': 'Dining Room'
                },

            'Pantry' : {
                'south': 'Dining Room',
                'item': 'cookie'
                }
            }


def show_instructions():
    """ print a main menu & commands """
    print('''
RPG Game
========
Commands:
    go [direction]
    get [item]
''')

def show_status():
    """ print the player's current status """
    print('----------------------------')
    print(f'You are in the {current_room}')
    print(f'Inventory: {inventory}')
    if "item" in rooms[current_room]:
        print(f'You see a {map[current_room]["item"]}')
    print('----------------------------')

def sub_go(room, direction):
    
    if direction in map[room]:
        new_room = map[room][direction]

    else:
        print("You can't go that way.")

    return new_room

def sub_get(room, item, inventory):
    
    if item in map[room]:
        new_inventory = inventory + item
        print(f"Got the {item}")
        del map[room][item]

    else:
        print("You can't get the {item}.")
    
    return new_inventory









def main():

    while True:

        show_status()

        move = ''

        while move == '':
            move = input('> ')

        move = move.lower().split(" ", 1)

        if move[0] == 'go':
            current_room = sub_go(current_room, move[1])

        if move[0] == 'get':
            inventory = sub_get(current_room, move[1], inventory)

    

    pass

if __name__ == "__main__":
    main()
