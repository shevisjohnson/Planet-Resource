from .game_object import GameObject

class Resource(GameObject):
    symbol = 'R'
    def __init__(self):
        super().__init__()
