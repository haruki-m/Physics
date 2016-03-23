from visual import *
from visual.graph import *
from math import *
import ForceModule

rad = 0.054
thk = 0.2
ball = sphere(pos = (0,2.248,0), radius = rad, color = color.white)
ground = box(pos = (0,0,0), size=(25, thk, 25), color = color.green)

velocity = 18.57
ball.Cd = 0.248
ball.mass = 0.1424
ball.area = .00916
ball.vel = vector(0,velocity,0)

acc = ForceModule.F_weight(ball.mass)

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

delta_t = 0.005
t = 0.8333 ##Time when rocket reaches max velocity

maxHeight = 0
maxHeightTime = 0

aboveGround = ball.radius+thk/2

while ball.pos.y>=aboveGround:
    rate(200)
    
    acc = (ForceModule.F_drag(ball)+ForceModule.F_weight(ball.mass))/ball.mass    
    ball.vel = ball.vel + acc * delta_t
    ball.pos = ball.pos + ball.vel * delta_t

    if maxHeight < ball.pos.y:
        maxHeight = ball.pos.y
        maxHeightTime = t

    f1.plot(pos=(t, ball.pos.y))
    f2.plot(pos=(t, ball.vel.y))
    f3.plot(pos=(t, acc.y))
    
    t=t+delta_t

print("Max Height: %4.2f" % maxHeight)
print("Time of Max Height: %4.2f" % maxHeightTime)
print("Time of Flight: %4.2f" % t)
