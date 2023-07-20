from .dragon import Dragon


class BodyguardDragon(Dragon):
    """BodyguardDragon provides protection to other Dragons."""

    name = 'Bodyguard'
    # OVERRIDE CLASS ATTRIBUTES HERE
    # BEGIN 3.2
    implemented = True  # Change to True to view in the GUI
    food_cost=4
    is_container=True
    def __init__(self, armor=2):
        Dragon.__init__(self, armor)
        self.contained_dragon = None  # The Dragon hidden in this bodyguard
        self.armor=2
    def can_contain(self, other):
        if self.contained_dragon is None and other.is_container==False and self.is_container:
            return True
        return False
        # BEGIN 3.2
        
        # END 3.2

    def contain_dragon(self, dragon):
        self.contained_dragon=dragon
        # BEGIN 3.2
        "*** YOUR CODE HERE ***"
        # END 3.2

    def action(self, colony):
        if self.contained_dragon is not None:
            self.contained_dragon.action(colony)
        # BEGIN 3.2
        
        # END 3.2
