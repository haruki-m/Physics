'''
Haruki Moriguchi
10/24/2014

'''

from visual import *
from math import *

## set scene
scene = display(center=(50,0,0))
scene.forward=(0,-0.2,-1)

## create field
ground=box(pos=(50,-5,0), size=(120,10,100), color=color.green)
wall=box(pos=(94.5,11.3/2,0), size=(2,11.3,70.1), color=color.green)

## change these variables
initialVel = 45
angle = 20

def run(vel):

    ## create ball and its trail
    ball=sphere(pos=(0,1,0), radius=1)
    ball.trail = curve(color=color.yellow)

    ## assign velocity to parameter
    velocity = vel

    ## break velocity into its components
    x_component = velocity*cos(radians(angle))
    y_component = velocity*sin(radians(angle))

    g = vector(0,-9.8,0)
    ball.vel = vector(x_component,y_component,0)

    delta_t=0.01
    t=0

    while ball.pos.y>0:
        rate(100)

        ball.vel = ball.vel + g * delta_t
        ball.pos = ball.pos + ball.vel * delta_t
        ball.trail.append(pos=ball.pos)

        ## if the ball hits the wall, make it bounce off
        if ball.pos.y<wall.size.y and ball.pos.x>wall.pos.x-0.5*wall.size.x and ball.pos.x<wall.pos.x+0.5*wall.size.x:
            ball.vel.x = -ball.vel.x
        t = t + delta_t
    print("Time: %4.2f" % (t))
    print("Range: %6.1f m" % (ball.pos.x))
    print("Velocity: %4.1f m/s" % (velocity))    
        

run(initialVel)
