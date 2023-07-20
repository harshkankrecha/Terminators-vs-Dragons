from .dragon import Dragon
from .scuba_thrower import ScubaThrower
from ..fighter import Fighter
from utils import terminators_win

class DragonKing(ScubaThrower):  # You should change this line
    # END 4.3
    """The King of the colony. The game is over if a terminator enters his place."""
    has_damage_doubled=True
    name = 'King'
    food_cost=7
    # OVERRIDE CLASS ATTRIBUTES HERE
    # BEGIN 4.3
    implemented = True  # Change to True to view in the GUI
    instantiated=False
    # END 4.3

    def __init__(self, armor=1):
        self.is_king=False
        if DragonKing.instantiated==False:
            DragonKing.instantiated=True
            self.armor=armor   
            self.is_king=True    

        # BEGIN 4.3
        "*** YOUR CODE HERE ***"
        
        # END 4.3

    def action(self, colony):
        """A dragon king throws a stone, but also doubles the damage of dragons
        in his tunnel.

        Impostor kings do only one thing: reduce their own armor to 0.
        """
        # BEGIN 4.3
        "*** YOUR CODE HERE ***"
        # END 4.3
        if self.is_king:
            ScubaThrower.action(self,colony)
            current_pos = self.place
            current_pos = current_pos.exit
            while current_pos is not None:
                if current_pos.dragon is not None:
                    if not current_pos.dragon.has_damage_doubled:
                        current_pos.dragon.damage *= 2
                        current_pos.dragon.has_damage_doubled = True
                    if current_pos.dragon.is_container and current_pos.dragon.contained_dragon is not None and not current_pos.dragon.contained_dragon.has_damage_doubled:
                        current_pos.dragon.contained_dragon.damage *= 2
                        current_pos.dragon.contained_dragon.has_damage_doubled = True
                current_pos = current_pos.exit

        else:
            self.reduce_armor(self.armor)

    def reduce_armor(self, amount):
        Fighter.reduce_armor(self,amount)       
        if self.is_king and self.armor<=0:
            terminators_win()

            

        """Reduce armor by AMOUNT, and if the True DragonKing has no armor
        remaining, signal the end of the game.
        """
        # BEGIN 4.3
        "*** YOUR CODE HERE ***"
