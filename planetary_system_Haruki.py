from visual import *
from visual.graph import *
from math import *

##Haruki Moriguchi

##Constants
AU = 1.496*pow(10,11)
EARTH_MASS = 5.98*pow(10,24)
G = 6.67*pow(10,-11)

##Planetary Objects
sun = sphere(pos=(0,0,0), radius=pow(10,9), color=color.yellow)
planet = sphere(pos=(0.5*AU,0,0), radius=5*pow(10,8), color=color.green)

##Function
def F_gravity(obj1,obj2):
    d = obj2.pos-obj1.pos
    r = d.norm()
    F_gravity = -G*obj1.mass*obj2.mass*r/d.mag2
    return F_gravity

##Graphs
Energy_gd = gdisplay(x=500,y=0,height=200,title="Total Energy",
                     xtitle="time (sec)", ytitle="Energy (J)",
                     background=color.white,foreground=color.black)
f1 = gcurve(color=color.blue)

AngMomentum_gd = gdisplay(x=500,y=200,height=200,title="Angular Momentum",
                     xtitle="time (sec)", ytitle="Angular Momentum (rad/s)",
                     background=color.white,foreground=color.black)
f2 = gcurve(color=color.orange)

##Planetary Objects
sun.mass = 1.989*pow(10,30)
planet.mass = 0.1*EARTH_MASS
planet.vel = vector(0,47085.21048,0)

t = 0
delta_t = 3600*12

aphelion = vector(0,0,0)
perihelion = sun.pos-planet.pos

while t<(3600*24*365*4):
    ##rate(100)

    ##Acceleration, velocity, and position
    acc = F_gravity(sun,planet)/planet.mass
    planet.vel = planet.vel+acc*delta_t
    planet.pos = planet.pos+planet.vel*delta_t

    ##Energy and angular momentum
    d = sun.pos-planet.pos
    
    kinetic = 0.5*planet.mass*planet.vel.mag2
    potential = -G*planet.mass*sun.mass/d.mag
    energy = kinetic+potential

    p = planet.mass*planet.vel
    angMomentum = cross(d, p)

    ##Calculate aphelion and perihelion
    if(planet.pos.mag-sun.pos.mag)>aphelion.mag:
        aphelion = planet.pos-sun.pos
    if(planet.pos.mag-sun.pos.mag)<perihelion.mag:
        perihelion = planet.pos-sun.pos
        
    ##Plot Graphs
    f1.plot(pos=(t, energy))
    f2.plot(pos=(t, angMomentum.mag))

    t+=delta_t
    
##Calculate eccentricity
a = (aphelion.mag+perihelion.mag)/2
eccentricity = (a-perihelion.mag)/a

print("Eccentricity: %4.5f" % eccentricity)
