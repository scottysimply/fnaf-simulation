from digraph import DiGraph
import random

class Animatronic:
    def __init__(self, name: str, ai: int, rooms: DiGraph, move_time: float = 4.97, max_ai: int = 20):
        self.name = name
        self.ai = ai
        self.rooms = rooms
        self.move_time = move_time
        self.max_ai = max_ai
        # key of current room
        self.current_room = ""

    def move(self):
        number = random.randint(1, self.max_ai)
        if self.ai >= number:
            # pick random place to move
            adj = self.rooms.adjacency[self.current_room]
            self.current_room = random.choice(adj)
            return True
        return False