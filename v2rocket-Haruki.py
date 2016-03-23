## Haruki Moriguchi

from visual import *
from visual.graph import *
from math import *
import ForceModule

rad = 0.8255 ##Given diameter = 1.651 m
thk = 0.2
ball = sphere(pos = (0,7,0), radius = rad, color = color.white) ##The rocket length is 14m, so assume cm is at 7m
ground = box(pos = (0,0,0), size=(25, thk, 25), color = color.green)

## Rocket Properties
velocity = 0 #starts at rest
ball.Cd = 0.245
ball.mass = 13000 #kg
ball.area = math.pow(rad,2)*math.pi #m^2
ball.vel = vector(0,velocity,0)
ball.fuelMass = 8610 #kg
ball.r = 130 #kg/s
burnTime = 65 #t
ball.uex = vector(0,1880,0) #m/s

## Create Graphs
pos_gd = gdisplay(x=400, y=0, height=200, title="Position of Rocket",
                  xtitle="time (sec)", ytitle="position (m)",
                  background=color.white,foreground = color.black)
f1 = gcurve(color=color.blue)
vel_gd=gdisplay(x=400, y=200, height=200, title="Velocity of Rocket",
                xtitle="time (sec)", ytitle="velocity (m/s)",
                background=color.white,foreground = color.black)
f2=gcurve(color=color.orange)
acc_gd = gdisplay(x=400, y=400, height=200, title="Acceleration of Rocket",
                  xtitle= "time (sec)", ytitle="acceleration (m/s/s)",
                  background=color.white,foreground = color.black)
f3 = gcurve(color=color.green)

## Set Delta_t and t
delta_t = 0.005
t = 0

maxHeight = 0
maxVel = 0

aboveGround = ball.radius+thk/2

while ball.pos.y>=aboveGround:

    #rate(100)
    
    if ball.r*t < ball.fuelMass: ## As long as there is still fuel
        ball.mass = ball.mass - ball.r*delta_t
        acc = (ForceModule.F_thrust(ball)+ForceModule.F_drag(ball)+ForceModule.F_weight(ball.mass))/ball.mass
        #acc = (ForceModule.F_thrust(ball)+ForceModule.F_weight(ball.mass))/ball.mass
        #acc = (ForceModule.F_thrust(ball))/ball.mass
        maxVel = ball.vel.y ## max velocity is right after rocket runs out of fuel
    else: ## After rocket runs out of fuel
        acc = (ForceModule.F_drag(ball)+ForceModule.F_weight(ball.mass))/ball.mass
        #acc = (ForceModule.F_weight(ball.mass))/ball.mass
    
    ball.vel = ball.vel + acc * delta_t
    ball.pos = ball.pos + ball.vel * delta_t

    ## find max height
    if maxHeight < ball.pos.y:
        maxHeight = ball.pos.y
    
    f1.plot(pos=(t, ball.pos.y))
    f2.plot(pos=(t, ball.vel.y))
    f3.plot(pos=(t, acc.y))
    
    t=t+delta_t

maxHeight += 7 ##add 7 because the rocket had an additional 7m from the center

print("Max Velocity: %4.2f" % maxVel + " m/s")
print("Max Height: %4.2f" % maxHeight + " m" )
print("Time of Flight: %4.2f" % t + " seconds")
