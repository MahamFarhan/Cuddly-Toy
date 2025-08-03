from cuddly_toy import CuddlyToy
class Bunny(CuddlyToy):
    def __init__(self, name, color, size):
        super().__init__(name, color, size)

    def make_sound(self):
        return "Squeak! I'm a bunny rabbit!"