# A Black_Hole is derived from Simulton; it updates by removing
#   any Prey whose center is contained within its radius
#  (returning a set of all eaten simultons), and
#   displays as a black circle with a radius of 10
#   (width/height 20).
# Calling get_dimension for the width/height (for
#   containment and displaying) will facilitate
#   inheritance in Pulsator and Hunter

from simulton import Simulton
from prey import Prey


class Black_Hole(Simulton):
    radius = 10
    
    def __init__(self, x, y):
        Simulton.__init__(self, x, y, Black_Hole.radius*2, Black_Hole.radius*2)
        
    def update(self, model):
        swallowed = model.find(lambda x: isinstance(x, Prey) and self.contains(x.get_location()))
        for prey in swallowed:
            model.remove(prey)
        return swallowed
        
    def display(self, canvas):
        canvas.create_oval(self._x-self._width/2, self._y-self._height/2, self._x+self._width/2, self._y+self._height/2, fill='Black')   
        
    def contains(self, xy):
        return abs(xy[0] - self._x) <= self._width/2 and abs(xy[1] - self._y) <= self._height/2