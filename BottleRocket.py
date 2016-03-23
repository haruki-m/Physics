from visual import *
from math import *
from visual.graph import *
import ForceModule

ball = sphere(pos=(0,1,0), radius=0.5, color=color.cyan)
wall = box(pos=(0,0,0), size=(12,0.2,12), color=color.green)
ball.vel = vector(0, 0, 0)
ball.Cd=0.205
ball.area=.0106
ball.accel= vector(0,0,0)
ball.Uex=vector(0,0,0)
ball.R = 0
watermass=0.5
ball.mass=.1889+watermass
ball.neck=.011
airvolume=.0015
airpressure=310264.08
thrust=0
weight=0
drag=0
vscale = 0.1
varr = arrow(pos=ball.pos, axis=vscale*ball.vel, color=color.red)
pos_gd = gdisplay(x=400,y=0,height = 200,title="Position of Ball",xtitle="time (s)",ytitle="Position (m)",
                  background=color.white,foreground=color.black)
f1=gcurve(color=color.blue)
vel_gd = gdisplay(x=400,y=220,height = 200,title="Velocity of Ball",xtitle="time (s)",ytitle="Velocity (m/s)",
                  background=color.white,foreground=color.black)
f2=gcurve(color=color.red)
accelerationDisplay = gdisplay(x=400, y=440, height=200, title="Acceleration of Ball", xtitle="Time (s)", ytitle = "Acceleration (m/s/s)", background=color.white, foreground=color.black)
f3 = gcurve(color=color.cyan)
deltat = 0.05
maxheight = 0
maxvel=0
t=0.0
while ball.pos.y>=0:
    rate(100)
    f1.plot(pos=(t,ball.pos.y))
    f2.plot(pos=(t,ball.vel.y))
    f3.plot(pos = (t, ball.accel.y))
    if ball.pos.y>maxheight:
        maxheight=ball.pos.y
    if ball.vel.y>maxvel:
        maxvel=ball.vel.y
    varr.pos = ball.pos
    varr.axis = vscale*ball.vel
    if watermass>0:
        deltat=0.001
        airpressure=airpressure*pow(((0.6889+((0.6889-ball.mass)/1000))/0.6889),-1.4)
        ball.Uex.y=sqrt((2*(airpressure-310264.08))/1000)
        ball.R =1000*math.pi*pow(ball.neck,2)*ball.Uex.y
        watermass=watermass-ball.R*deltat
        ball.mass=.1889+watermass
        Fnet=ForceModule.F_thrust(ball)+ForceModule.F_weight(ball)+ForceModule.F_drag(ball)
        thrust=ForceModule.F_thrust(ball)
        weight=ForceModule.F_weight(ball.mass)
        drag=ForceModule.F_drag(ball)
    else:
        deltat=0.0001
        Fnet=ForceModule.F_weight(ball.mass)+ForceModule.F_drag(ball)
    ball.accel = Fnet/ball.mass
    ball.vel = ball.vel + ball.accel*deltat
    ball.pos = ball.pos + ball.vel * deltat
    t = t + deltat
#print "Max Velocity: "
print (maxvel)
#print "Max Height: "
print (maxheight)
#print "Time in Air: "
print (t)
