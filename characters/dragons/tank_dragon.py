from .bodyguard_dragon import BodyguardDragon
from .dragon import Dragon

class TankDragon(BodyguardDragon):
    """TankDragon provides both offensive and defensive capabilities."""

    name = 'Tank'
    damage = 1
    # OVERRIDE CLASS ATTRIBUTES HERE
    # BEGIN 3.3
    implemented = True  # Change to True to view in the GUI
    food_cost=6
    armor=2
    is_container=True
    # END 3.3
    def action(self, colony):
        if self.contained_dragon is not None:
            #self.contained_dragon.damage+=1
            self.contained_dragon.action(colony)
        active_terminators=[obj for obj in self.place.terminators ]       
        for each_terminator in active_terminators:            
            each_terminator.reduce_armor(self.damage)        
        

        # BEGIN 3.3
        "*** YOUR CODE HERE ***"

