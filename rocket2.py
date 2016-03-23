from visual import *
from visual.graph import *
from math import *
import ForceModule

rad=0.054
thk = 0.2
ball = sphere(pos=(0,rad+0.1,0), radius = rad, color=color.white)
ground = box(pos=(0,0,0), size=(25, thk, 25), color = color.green)
waterVolume = .5
waterConversionFactor = 1


waterMass = .5 #kg
velocity = 0

ball.Cd = 0.242
ball.justMass = 0.1424
ball.mass= ball.justMass + waterMass
ball.area = .01061
ball.vel = vector(0,velocity,0)
ball.uex = vector(0,0,0)


initialRocketMass=waterMass + ball.mass 
initialPressure = 45 * 6894.75729 ## pascals
initialAirVolume = 2 - waterMass
bottleNeck = .0105 ##m
densityOfWater = 1000 ##kg/m3
Patm = 15 * 6894.75729  ##pascals


pos_gd = gdisplay(x=400, y=0, height=200, title="Position of Rocket", xtitle="time (sec)", ytitle="position (m)",background=color.white,foreground = color.black)
f1 = gcurve(color=color.blue)

vel_gd=gdisplay(x=400, y=200, height=200, title="Velocity of Rocket", xtitle="time (sec)", ytitle="velocity (m/s)",background=color.white,foreground = color.black)
f2=gcurve(color=color.orange)

acc_gd = gdisplay(x=400, y=400, height=200, title="Acceleration of Rocket", xtitle= "time (sec)", ytitle="acceleration (m/s/s)",background=color.white,foreground = color.black)

f3 = gcurve(color=color.green)

drag_gd = gdisplay(x=400, y=600, height=200, title="Drag Force acting on the Rocket", xtitle= "time (sec)", ytitle="drag force (N)",background=color.white,foreground = color.black)

f4 = gcurve(color=color.green)

delta_t = 0.001
t=0

aboveGround = ball.radius+thk/2
maxheight = 0
drag_total = 0
drag_denominator = 0
while ball.pos.y>=aboveGround:
    rate(200)
    
    PT = initialPressure * pow (    (initialAirVolume + (initialRocketMass - ball.mass)/densityOfWater)/initialAirVolume ,-1.4)
    if (ball.mass > ball.justMass):

        delta_t = 0.0001
        ball.uex.y = sqrt(  (2*(PT - Patm))/(densityOfWater))
        ball.r = densityOfWater * pi * bottleNeck*bottleNeck * ball.uex.y
        rocketThrust = ForceModule.F_thrust(ball)
        acc = (ForceModule.F_thrust(ball)+ForceModule.F_drag(ball)+ForceModule.F_weight(ball.mass))/ball.mass
        ball.mass = ball.mass - ball.r * delta_t
    else:
        acc = (ForceModule.F_weight(ball.mass)+ForceModule.F_drag(ball))/ball.mass
        delta_t = 0.005
        

    ball.vel=ball.vel+acc*delta_t
    ball.pos=ball.pos+ball.vel*delta_t

    f1.plot(pos=(t, ball.pos.y))
    f2.plot(pos=(t, ball.vel.y))
    f3.plot(pos=(t, acc.y))
    f4.plot(pos=(t, ForceModule.F_drag(ball).y))

    t=t+delta_t
    if maxheight < ball.pos.y:
        maxheight = ball.pos.y
        drag_total = drag_total + ForceModule.F_drag(ball).y
        drag_denominator = drag_denominator + 1

print("Maximum Height: " + str(maxheight))
print("Flight Time: " + str(t))
print(drag_total/drag_denominator)
