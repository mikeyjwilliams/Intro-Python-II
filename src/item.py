""" 
Item.py
base class for specialized item types to be declared later.

"""


class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return f'{self.name}'

    def item_description(self):
        return f'{self.description}'
