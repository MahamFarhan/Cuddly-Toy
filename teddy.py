from cuddly_toy import CuddlyToy

class Teddy(CuddlyToy):
    def __init__(self, name, color, size):
        super().__init__(name, color, size)
        #built-in Python function that gives you access to methods in a parent (super) 
        # class from inside a child class.
    def make_sound(self):
        return "Growl! I'm a teddy bear!"