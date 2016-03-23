'''
Haruki Moriguchi
9/26/2014

'''

from visual import *
from visual.graph import *
from math import *

##create ball and ground
rad=0.5
thk=0.2
ball = sphere(pos=(0,rad+thk/2,0), radius=rad, color=color.red)
ground = box(pos=(0,0,0), size=(25, thk, 25), color=color.green)

##set velocity and acceleration
velocity = 25
g = vector(0,-9.8,0)
ball.vel = vector(0,velocity,0)

##arrow
vscale = 0.1
varr = arrow(pos=ball.pos, axis=vscale*ball.vel, color=color.cyan)

##Position and velocity graphs
pos_gd = gdisplay(x=400, y=0, height=200, title="Position of Ball", xtitle=
                  "time (sec)", ytitle="position (m)", background=color.white,
                  foreground=color.black)
f1=gcurve(color=color.blue)

vel_gd = gdisplay(x=400, y=220, height=200, title="Velocity of Ball",
                  xtitle="time (s)", ytitle="Velocity (m/s)",
                  background=color.white, foreground=color.black)
f2=gcurve(color=color.orange)

##delta T
delta_t = 0.005
t=0

##stop the program when the surface of the ball hits the ground
aboveGround = ball.radius+thk/2

while ball.pos.y>=aboveGround:
    rate(200)

    ##change the position and the velocity of the ball and arrow
    ball.vel=ball.vel+g*delta_t
    ball.pos=ball.pos+ball.vel*delta_t

    varr.pos=ball.pos
    varr.axis=vscale*ball.vel

    ##plot graphs
    f1.plot(pos=(t, ball.pos.y))
    f2.plot(pos=(t, ball.vel.y))

    t=t+delta_t


