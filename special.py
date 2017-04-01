# Special is a Prey similar to Special and floater
# except it moves faster and has a larger radius.
# It starts off as an orange circle but changes 
# to a random color every 15 cycles.

from prey import Prey
import random

class Special(Prey):
    radius = 10
    max_count = 15
    
    def __init__(self, x, y):
        Prey.__init__(self, x, y, Special.radius*2, Special.radius*2, 0, 10)
        Special.randomize_angle(self)
        self.counter = 0
        self.color = 'Orange'
        
    def update(self, model):
        self.counter += 1
        if self.counter == Special.max_count:
            self.color = "#"+str(hex(random.randint(20,255)))[2:]+str(hex(random.randint(20,255)))[2:]+str(hex(random.randint(20,255)))[2:]
            self.counter = 0
        self.move()   
                
    def display(self, canvas):
        canvas.create_oval(self._x-Special.radius, self._y-Special.radius, self._x+Special.radius, self._y+Special.radius, fill=self.color)
