class CuddlyToy:
    def __init__(self, name, color, size):
        self.name = name
        self.color = color
        self.size = size

    def describe(self):
        return f"{self.name} is a {self.color} cuddly toy of size {self.size}."
    # a default version of make_sound and job methods for all toys
    def make_sound(self):
        return "Generic cuddly toy sound!"
    def job(self):
        return "I do nothing special, just sit here and look cute!"