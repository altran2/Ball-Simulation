# A Floater is Prey; it updates by moving mostly in
#   a straight line, but with random changes to its
#   angle and speed, and displays as ufo.gif (whose
#   dimensions (width and height) are computed by
#   calling .width()/.height() on the PhotoImage


# from PIL.ImageTk import PhotoImage
from prey import Prey
from random import random


class Floater(Prey):
    radius = 5
    
    def __init__(self, x, y):
        Prey.__init__(self, x, y, Floater.radius*2, Floater.radius*2, 0, 5)
        Floater.randomize_angle(self)
        
    def update(self, model):
        if random() <= 0.3:
            new_speed = min(7, max(3, self.get_speed() + (random() - 0.5)))
            new_angle = self.get_angle() + (random() - 0.5)
            self.set_velocity(new_speed, new_angle)
        self.move()
    
    def display(self, canvas):
        canvas.create_oval(self._x-Floater.radius, self._y-Floater.radius, self._x+Floater.radius, self._y+Floater.radius, fill='Red')