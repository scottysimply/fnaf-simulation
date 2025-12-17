from animatronic import Animatronic

class Pizzeria:
    def __init__(self, animatronic: Animatronic, starting_room: str):
        self.animatronic = animatronic
        self.starting_room = starting_room
        self.animatronic.current_room = starting_room

    def reset(self):
        self.animatronic.current_room = self.starting_room