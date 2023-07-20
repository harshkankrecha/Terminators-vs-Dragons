from .dragon import Dragon
import random

class HungryDragon(Dragon):
    """HungryDragon will take three turns to digest a Terminator in its place.
    While digesting, the HungryDragon can't eat another Terminator.
    """
    name = 'Hungry'
    # OVERRIDE CLASS ATTRIBUTES HERE
    food_cost=4
    armor=1
    time_to_digest=3
    # BEGIN 2.3
    implemented = True  # Change to True to view in the GUI

    # END 2.3

    def __init__(self, armor=1):
        # BEGIN 2.3
        "*** YOUR CODE HERE ***"
        self.digesting=0
        # END 2.3

    def eat_terminator(self, terminator):
        terminator.reduce_armor(terminator.armor)
        #terminator.place.remove_fighter(terminator)        
        #terminator.death_callback()
        self.digesting=self.time_to_digest
        # BEGIN 2.3
        "*** YOUR CODE HERE ***"
        # END 2.3
    def action(self, colony):
        if self.digesting==0:
            if len(self.place.terminators)!=0:
                active_terminator=random.choice(self.place.terminators)
                self.eat_terminator(active_terminator)


        else:
            self.digesting-=1
        # BEGIN 2.3
        "*** YOUR CODE HERE ***"

