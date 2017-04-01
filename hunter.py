# A Hunter is derived from a Mobile_Simulton and a Pulsator; it updates
#   like a Pulsator, but it also moves (either in a straight line
#   or in pursuit of Prey), and displays as a Pulsator.


from pulsator import Pulsator
from mobilesimulton import Mobile_Simulton
from prey import Prey
from math import atan2


class Hunter(Pulsator,Mobile_Simulton):
    chase_distance = 200
    
    def __init__(self, x, y):
        Pulsator.__init__(self, x, y)
        Mobile_Simulton.__init__(self, x, y, self.radius*2, self.radius*2, 0, 5)
        self.randomize_angle()
    
    def update(self, model):
        swallowed = Pulsator.update(self, model)
        targets = model.find(lambda x: isinstance(x, Prey))
        for prey in targets:
            if self.distance(prey.get_location()) <= self.chase_distance:                
                dist, closest = min([(self.distance(prey.get_location()), prey) for prey in targets])
                hunter_x, hunter_y = self.get_location()
                prey_x, prey_y = closest.get_location()
                self.set_angle(atan2(prey_y-hunter_y, prey_x-hunter_x))
        self.move()
        return swallowed
