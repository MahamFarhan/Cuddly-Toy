from teddy import Teddy
from bunny import Bunny

class EngineDriver(Teddy):
    def __init__(self, size):
        super().__init__("Engine Driver", "Red", size)
    def job(self):
        return "I'm an enginge driver, I change gears!"
        
class Gardener(Teddy):
    def __init__(self, size):
        super().__init__("Gardener", "Green", size)
    def job(self):
        return "I'm a gardener, I cut vegetables!"
class Clown(Bunny):
    def __init__(self, size):
        super().__init__("Clown", "White", size)
    def job(self):
        return "I'm a clown, I make children laugh!"
class BankManager(Bunny):
    def __init__(self, size):
        super().__init__("Bank Manager", "Black", size)
    def job(self):
        return "I'm a bank manager, I authorize loans!"