from .dragon import Dragon

class NinjaDragon(Dragon):
    """NinjaDragon does not block the path and damages all terminators in its place."""
    name = 'Ninja'
    damage = 1
    food_cost=5
    armor=1
    # OVERRIDE CLASS ATTRIBUTES HERE
    blocks_path=False
    # BEGIN 2.4
    implemented = True  # Change to True to view in the GUI
    # END 2.4
    def action(self, colony):
        active_terminators=[obj for obj in self.place.terminators ]       
        for each_terminator in active_terminators:            
            each_terminator.reduce_armor(self.damage)              
                    
            
                
        
        # BEGIN 2.4
        "*** YOUR CODE HERE ***"
