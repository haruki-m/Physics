from visual import *
from visual.graph import *
from math import*
import ForceModule

## Haruki Moriguchi
## 4/8/2015

rad = 0.07 ##m
length = 0.37 ##m- length of rocket. Center of mass is 21.5cm from the top of the rocket
thk = 0.2
ball = sphere(pos = (0,0.155,0), radius = rad, color = color.white) ##Rocket's center of mass is 15.5cm from the bottom
ground = box(pos = (0,0,0), size=(25, thk, 25), color = color.green)

## 1. Set the initial conditions:
velocity = 0.0 ##m/s
angle = 45 ##degrees
waterVol = 0.640 ##L
waterMass = waterVol ##kg
waterDensity = 1000.0 #kg m^-3
airPressure = 15*6894.75729 ##pascals from psi
initialPressure = 75*6894.75729 ##pascals from psi
initialMass = 0.1424+waterMass ##rocket.mass + mass of water
initialVolume = (2.0 - waterVol)/1000 ##m^3

ball.mass = initialMass
ball.pressure = initialPressure
ball.airVol = initialVolume
ball.bottleNeck = 0.0105 ##m

ball.Cd = 0.248
ball.area = 0.012 ##m^2
ball.vel = vector(0,velocity,0)
ball.uex = vector(0,0,0)
ball.r = 0
ball.angle = angle

##Create Graphs
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

##Set initial time, max height, initial max velocity, time of max height
t = 0
maxHeight = 0.000
maxVel = 0.000
maxHeightTime = 0.000

while ball.pos.y>=0:
    ##rate(100)

    ## 2. While the bottle contains water,
    ##      compute the exhuast speed, mass rate, and thrust:
    if ball.mass > initialMass-waterMass: ##If there's still water in the rocket
        delta_t = 0.00001
        acc = (ForceModule.F_thrust(ball)+ForceModule.F_drag(ball)+ForceModule.F_weight(ball.mass))/ball.mass
        ball.uex.y = sqrt((2*(ball.pressure-airPressure))/waterDensity)
        ball.r = waterDensity*pi*pow(ball.bottleNeck, 2)*ball.uex.y
        
        ##4. Update the rocket's mass and internal pressure
        ball.pressure = initialPressure*pow(((initialVolume+((initialMass-ball.mass)/waterDensity))/initialVolume),-1.4)
        ball.mass = ball.mass - ball.r*delta_t

        maxVel = ball.vel.y ##max velocity is right after rocket runs out of water
    else: ##After rocket runs out of water
        delta_t = 0.0001
        acc = (ForceModule.F_drag(ball)+ForceModule.F_weight(ball.mass))/ball.mass

    ##3. Compute the trajectory as done previously
    ball.vel = ball.vel + acc * delta_t
    ball.pos = ball.pos + ball.vel * delta_t

    ## find max height
    if maxHeight < ball.pos.y:
        maxHeight = ball.pos.y
        maxHeightTime = t

    f1.plot(pos=(t, ball.pos.y))
    f2.plot(pos=(t, ball.vel.y))
    f3.plot(pos=(t, acc.y))

    t=t+delta_t

ball.pressure /= 6894.75729 ##convert back to psi
maxHeight += 0.215 ##the top of the rocket is 21.5cm above the center of mass
distanceTraveled = ball.pos.x

#print("Max Speed: %4.2f" % maxVel + " m/s")
print("Max Height: %4.2f" % maxHeight + " m")
#print("Time when Rocket Reaches Max Height: %4.2f" % maxHeightTime + " seconds")
print("Time of Flight: %4.2f" % t + " seconds")
#print("Final Pressure inside Rocket: %4.2f" % ball.pressure + " psi")
#print("Final Total Mass of Rocket: %4.4f" % ball.mass + " kg")
print("Distance Traveled: %4.4f" % distanceTraveled + " m")
