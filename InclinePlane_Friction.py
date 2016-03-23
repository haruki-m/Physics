from visual import *
from visual.graph import *
from math import *

##Input values
initVel = float(input("Initial velocity (m/s):"))

theta= float(input("Angle of incline (deg):"))
theta_rad=radians(theta)

mu_k = float(input("Coeff. of kinetic friction:"))
mu_s = 1.2*mu_k

##Set up scene
floor = box(pos=(0,0,0),height=0.5,length=50,width=25,color=color.green)
initCratePos=vector(-20,2.25,0)
crate = box(pos=initCratePos,height=4,length=6,width=4,color=color.red)
crate.mass = 10.
crate.vel=vector(initVel,0,0).rotate(theta_rad,(0,0,1))

scene.forward = (0,-.5,-.866)

##Rotate floor,crate so make incline
floor.rotate(angle=theta_rad,axis=(0,0,1),origin=crate.pos)
crate.rotate(angle=theta_rad,axis=(0,0,1))

##Force functions
g = vector(0,-9.8,0)
F_g = crate.mass*g

def F_friction(F_normal,mu_k,velocity):
    F_friction = -mu_k*F_normal.mag*norm(velocity)
    return F_friction

def F_normal(force,surface):
    ax= -surface.y/surface.mag
    ay=surface.x/surface.mag
    x=diff_angle(force,surface)-0.5*pi
    F_normal=force.mag*cos(x)*vector(ax,ay,0)
    return F_normal

##Graphs for x,v,a
gd_pos = gdisplay(x=430,y=0,height=200,title="Displacement",xtitle="time(s)",ytitle="d (m)",
                  background=color.white,foreground=color.black)
f1=gcurve(color=color.blue)
gd_vel = gdisplay(x=430,y=220,height=200,title="Velocity",xtitle="time(s)",ytitle="|v| (m/s)",
                  background=color.white,foreground=color.black)
f2=gcurve(color=color.red)
gd_acc = gdisplay(x=430,y=440,height=200,title="Acceleration",xtitle="time(s)",ytitle="|a| (m/s/s)",
                  background=color.white,foreground=color.black)
f3=gcurve(color=color.green)

##initialize
t=0
dt=0.01

##Loop while crate slides along surface
while crate.pos.x>=initCratePos.x:
    rate(200)

    ##Compute forces, acceleration
    F_n=F_normal(F_g,floor.axis)
    F_fr=F_friction(F_n,mu_k,crate.vel)
    F_net = F_g + F_n + F_fr
    crate.acc = F_net/crate.mass

    ##update position, velocity
    crate.pos = crate.pos + crate.vel*dt
    crate.vel = crate.vel + crate.acc*dt

    ##plot curves
    f1.plot(pos=(t,mag(crate.pos-initCratePos)))
    f2.plot(pos=(t,crate.vel.mag))
    f3.plot(pos=(t,crate.acc.mag))

    ##if static friction enough to stop, break loop
    if crate.vel.x<=0 and mu_s >= tan(theta_rad):
        break
    ##if crate slides off end of plane, break loop
    if crate.pos.x+0.5*crate.axis.x >= 0.5*floor.axis.x:
        break
    
    t = t + dt

##print out
print ("Distance traveled (m) = %.1f" % (mag(crate.pos-initCratePos)))
print ("Total time (s) = %.2f" % (t))

