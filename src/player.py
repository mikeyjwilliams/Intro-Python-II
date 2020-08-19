# Write a class to hold player information, e.g. what room they are in
# currently.
from room import Room


class Player:
    def __init__(self, name, current_room, pocket=[]):
        self.name = name
        self.current_room = current_room
        self.pocket = pocket

    def __str__(self):
        return f'{self.current_room}'

    def room_current(self):
        return f'{self.current_room}'

    def on_take(self, item):
        print(f'{self.name} picked up {item}')
        print(f'Now with great power comes great...')
        print(f'I am kidding...this is a game.')
        self.pocket.append(item)
