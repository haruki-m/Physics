##Haruki Moriguchi

from visual import *
from math import *

def F_weight(mass,planet="earth"):
    gravity={"earth":9.8,"moon":1.62}
    planet=planet.lower() 
    F_weight=mass*vector(0,-gravity[planet], 0)
    return F_weight

def F_drag(obj,air_density=1.204):
    F_drag = -0.5*obj.Cd*obj.area*air_density*obj.vel.mag*obj.vel
    return F_drag

def F_thrust(obj):
    F_thrust = obj.uex*obj.r
   ## F_thrust = rotate(F_thrust, -obj.angle, vector(0,0,1))
    return F_thrust

def F_gravity(obj1, obj2):
    d = obj2.pos-obj1.pos
    r = d.norm()
    G = 6.67*pow(10,-11)
    F_gravity = -G*obj1.mass*obj2.mass*r/d.mag2
    return F_gravity
