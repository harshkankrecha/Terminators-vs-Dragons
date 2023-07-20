from .thrower_dragon import ThrowerDragon
class ScubaThrower(ThrowerDragon):
    # ADD/OVERRIDE CLASS ATTRIBUTES HERE
    food_cost=6
    name="Scuba"
    implemented=True
    is_watersafe=True

    def __init__(self):
        self.armor=1
        
   
