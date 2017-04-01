import controller, sys
import model   #strange, but we need a reference to this module to pass this module to update

from ball      import Ball
from floater   import Floater
from blackhole import Black_Hole
from pulsator  import Pulsator
from hunter    import Hunter
from special   import Special 

# Global variables: declare them global in functions that assign to them: e.g., ... = or +=
running = False
step_check = False
cycle_count = 0
simultons = set()
object = None

#return a 2-tuple of the width and height of the canvas (defined in the controller)
def world():
    return (controller.the_canvas.winfo_width(),controller.the_canvas.winfo_height())

#reset all module variables to represent an empty/stopped simulation
def reset ():
    global running, cycle_count, simultons, object
    running = False
    step_check = False
    cycle_count = 0
    simultons = set()
    object = None

#start running the simulation
def start ():
    global running
    running = True

#stop running the simulation (freezing it)
def stop ():
    global running
    running = False

#tep just one update in the simulation
def step ():
    global running, step_check
    running = True
    step_check = True

#remember the kind of object to add to the simulation when an (x,y) coordinate in the canvas
#  is clicked next (or remember to remove an object by such a click)   
def select_object(kind):
    global object
    object = kind

#add the kind of remembered object to the simulation (or remove any objects that contain the
#  clicked (x,y) coordinate
def mouse_click(x,y):
    global things, object
    if object == 'Remove':
        for s in simultons:
            if s.contains((x,y)):
                remove(s)
                break
    else:
        add(eval(object+'('+str(x)+','+str(y)+')'))

#add simulton s to the simulation
def add(s):
    global simultons
    simultons.add(s)
    
# remove simulton s from the simulation    
def remove(s):
    global simultons
    simultons.remove(s)

#find/return a set of simultons that each satisfy predicate p    
def find(p):
    global simultons
    return {s for s in simultons if p(s)}

#call update for every simulton in the simulation
def update_all():
    global running, step_check, cycle_count, simultons
    if running:
        cycle_count += 1
        for s in list(simultons):
            s.update(model)
        if step_check:
            running = False
            step_check = False

#delete from the canvas every simulton in the simulation; then call display for every
#  simulton in the simulation to add it back to the canvas possibly in a new location: to
#  animate it; also, update the progress label defined in the controller
def display_all():
    for t in controller.the_canvas.find_all():
        controller.the_canvas.delete(t)
    
    for s in simultons:
        s.display(controller.the_canvas)
        
    controller.the_progress.config(text = str(cycle_count)+" updates/"+str(len(simultons))+" simultons")
    
